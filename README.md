## 🤖 AI Agent for Query Resolution
This project is an AI agent that answers user queries by retrieving information from a local SQL database, text documents, and real-time web searches. The agent is built using Python and the LangChain framework, leveraging Google's Gemini models.

## 🎯 Objective
The goal is to build an agent that accepts a user query, retrieves relevant structured data (SQL) and unstructured data (RAG), and augments it with real-time web search to synthesize a final, cited answer. This fulfills the requirements of Task A from the project brief.

## ✨ Features
Structured Data Retrieval: Connects to a SQLite database to answer specific questions about projects and employees.

Unstructured Data Retrieval (RAG): Searches a FAISS vector database of internal documents to answer conceptual questions.

Real-time Web Search: Uses SerpAPI to find up-to-the-minute information on the web.

Explainability: The agent's thought process is printed to the console, showing which tool it chose and why for each query.

## 🛠️ Project Setup and Installation
Follow these steps to set up and run the project locally.

Clone the Repository

git clone https://github.com/amanv13/Query-Resolution-AI-Agent.git
cd Query-Resolution-AI-Agent

Create and Activate Virtual Environment

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate

# Install Dependencies

pip install -r requirements.txt

# Set Up API Keys

Create a file named .env in the root of the project.

Add your API keys to the file in the following format:

GOOGLE_API_KEY="your_google_api_key_here"
SERPAPI_API_KEY="your_serpapi_key_here"

# Prepare Data Sources

First, create and populate the SQL database:

python setup_database.py

Next, process the documents and create the vector index:

python ingest.py

## 🚀 How to Run the Agent
Once the setup is complete, you can start the agent with the following command:

python agent.py

The agent will launch and you can begin asking questions at the You: prompt. Type exit to quit.

## 📊 Sample Queries & Outputs
Here are the outputs from the 6 required test queries, demonstrating the agent's ability to use its different tools.

<details>
<summary><strong>Query 1: Who is the lead for the project 'AI Agent Alpha'?</strong></summary>

Tool Used: Employee_and_Project_Database_Search

Final Answer: Bob is the lead for the project 'AI Agent Alpha'.

Agent's Thought Process:

> Entering new AgentExecutor chain...
Invoking: `Employee_and_Project_Database_Search` with `Who is the lead for the project AI Agent Alpha?`

> Entering new SQL Agent Executor chain...
Invoking: `sql_db_list_tables` with `{}`
employees, projects
Invoking: `sql_db_schema` with `{'table_names': 'projects'}`

CREATE TABLE projects (
    project_id INTEGER, 
    project_name TEXT NOT NULL, 
    status TEXT, 
    lead_id INTEGER, 
    PRIMARY KEY (project_id), 
    FOREIGN KEY(lead_id) REFERENCES employees (id)
)

Invoking: `sql_db_query` with `{'query': "SELECT e.employee_name FROM employees e JOIN projects p ON e.id = p.lead_id WHERE p.project_name = 'AI Agent Alpha'"}`
Error: (sqlite3.OperationalError) no such column: e.employee_name

Invoking: `sql_db_schema` with `{'table_names': 'employees'}`

CREATE TABLE employees (
    id INTEGER, 
    name TEXT NOT NULL, 
    role TEXT NOT NULL, 
    start_date TEXT, 
    PRIMARY KEY (id)
)

Invoking: `sql_db_query` with `{'query': "SELECT e.name FROM employees e JOIN projects p ON e.id = p.lead_id WHERE p.project_name = 'AI Agent Alpha'"}`
[('Bob',)]
Bob is the lead for the project AI Agent Alpha.
> Finished chain.

{'input': 'Who is the lead for the project AI Agent Alpha?', 'output': 'Bob is the lead for the project AI Agent Alpha.'}

</details>

<details>
<summary><strong>Query 2: How many projects are in progress?</strong></summary>

Tool Used: Employee_and_Project_Database_Search

Final Answer: There is 1 project in progress.

Agent's Thought Process:

> Entering new AgentExecutor chain...
Invoking: `Employee_and_Project_Database_Search` with `How many projects are in progress?`

> Entering new SQL Agent Executor chain...
Invoking: `sql_db_list_tables` with `{}`
employees, projects
Invoking: `sql_db_schema` with `{'table_names': 'projects'}`

CREATE TABLE projects (
    project_id INTEGER, 
    project_name TEXT NOT NULL, 
    status TEXT, 
    lead_id INTEGER, 
    PRIMARY KEY (project_id), 
    FOREIGN KEY(lead_id) REFERENCES employees (id)
)

Invoking: `sql_db_query` with `{'query': "SELECT COUNT(*) FROM projects WHERE status = 'In Progress'"}`
[(1,)]
There is 1 project in progress.
> Finished chain.

{'input': 'How many projects are in progress?', 'output': 'There is 1 project in progress.'}

</details>

<details>
<summary><strong>Query 3: What is the mission of the company?</strong></summary>

Tool Used: Document_and_Policy_Search

Final Answer: Our mission is to democratize access to information through intelligent systems. We believe in open-source collaboration and ethical AI development.

Agent's Thought Process:

> Entering new AgentExecutor chain...
Invoking: `Document_and_Policy_Search` with `company mission`
[Document(id='...', metadata={'source': 'docs/company_info.txt'}, page_content='Our mission is to democratize access to information through intelligent systems. We believe in open-source collaboration and ethical AI development. For support, please contact the AI engineering team.'), Document(id='...', metadata={'source': 'docs/project_brief.txt'}, page_content='...')]
Our mission is to democratize access to information through intelligent systems. We believe in open-source collaboration and ethical AI development.

</details>

<details>
<summary><strong>Query 4: What are the key technologies for Project AI Agent Alpha?</strong></summary>

Tool Used: Employee_and_Project_Database_Search (Incorrectly)

Final Answer: I am sorry, I was unable to find the key technologies for Project AI Agent Alpha in the available database. The database search failed because the necessary information is not present.

Agent's Thought Process:

> Entering new AgentExecutor chain...
Invoking: `Employee_and_Project_Database_Search` with `{'question': 'What are the key technologies for Project AI Agent Alpha?'}`

> Entering new SQL Agent Executor chain...
Invoking: `sql_db_list_tables` with `{}`
employees, projects
Invoking: `sql_db_schema` with `{'table_names': 'projects'}`

CREATE TABLE projects (...)

Invoking: `sql_db_query` with `{'query': "SELECT key_technologies FROM projects WHERE project_name = 'AI Agent Alpha'"}`
Error: (sqlite3.OperationalError) no such column: key_technologies
The query failed because the `key_technologies` column does not exist in the `projects` table. I need to find a way to answer the question without that column. I don't know.
> Finished chain.

{'input': 'What are the key technologies for Project AI Agent Alpha?', 'output': "The query failed because the `key_technologies` column does not exist in the `projects` table. I need to find a way to answer the question without that column. I don't know."}

(Note: This demonstrates a limitation. The agent incorrectly chose the SQL tool instead of the Document Search tool, which contains the answer.)

</details>

<details>
<summary><strong>Query 5: What is the current time in Mumbai?</strong></summary>

Tool Used: Web_Search

Final Answer: The current time in Mumbai is 9:53 PM.

Agent's Thought Process:

> Entering new AgentExecutor chain...
Invoking: `Web_Search` with `current time in Mumbai`
9:53 PM
The current time in Mumbai is 9:53 PM.

</details>

<details>
<summary><strong>Query 6: Who won the last cricket world cup?</strong></summary>

Tool Used: Web_Search (Implicitly)

Final Answer: Australia won the last Cricket World Cup.

</details>

