import os
from dotenv import load_dotenv

# --- Core LangChain components ---
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor, Tool

# --- LLM ---
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# --- Tool-specific components ---
from langchain_community.vectorstores import FAISS
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent

# ------------------ SETUP ------------------

load_dotenv()
print("✅ Environment variables loaded")

# UPDATED MODEL NAME
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", convert_system_message_to_human=True)
print("✅ LLM initialized")

# ------------------ TOOLS ------------------

# --- Tool 1: Vector Database Retriever ---
DB_FAISS_PATH = "faiss_index"
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
print("✅ FAISS vector database loaded")
vector_retriever = db.as_retriever(search_kwargs={"k": 2})
vector_db_tool = Tool(
    name="Document_and_Policy_Search",
    func=vector_retriever.invoke,
    description="Use this tool to search for information in company documents, project briefs, and internal policies."
)
print("✅ Vector DB tool created")

# --- Tool 2: SQL Database Tool ---
db_path = "company_data.db"
sql_db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
print("✅ SQL Database connection established")
sql_agent_executor = create_sql_agent(
    llm=llm,
    db=sql_db,
    agent_type="tool-calling",
    verbose=True
)
print("✅ SQL Agent Executor created")
sql_tool = Tool(
    name="Employee_and_Project_Database_Search",
    func=sql_agent_executor.invoke,
    description="Use this tool to find information about employees, projects, project status, and project leads. Input to this tool should be a full question."
)
print("✅ SQL tool created")

# --- Tool 3: Web Search Tool ---
web_search = SerpAPIWrapper()
print("✅ SerpAPI Wrapper initialized")
web_search_tool = Tool(
    name="Web_Search",
    func=web_search.run,
    description="Use this tool to find up-to-date information on the web, such as current events, weather, or information not found in internal documents."
)
print("✅ Web search tool created")


# ------------------ AGENT ASSEMBLY ------------------

tools = [vector_db_tool, sql_tool, web_search_tool]
print("✅ Tools assembled")

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. You must use the tools provided to answer the user's questions."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])
print("✅ Prompt template created")

agent = create_tool_calling_agent(llm, tools, prompt_template)
print("✅ Agent created")

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)
print("✅ Agent Executor created")


# ------------------ MAIN EXECUTION LOOP ------------------

print("\n--- Agent is ready! Type 'exit' to quit. ---")

while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Agent: Goodbye!")
            break
        
        response = agent_executor.invoke({"input": user_input})
        
        print(f"Agent: {response['output']}")
    except Exception as e:
        print(f"An error occurred: {e}")