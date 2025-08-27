AI Agent for Query Resolution
This project is an AI agent that answers user queries by retrieving information from a local SQL database, text documents, and real-time web searches. The agent is built using Python and the LangChain framework, leveraging Google's Gemini models.

Objective
The goal is to build an agent that accepts a user query, retrieves relevant structured data (SQL) and unstructured data (RAG), and augments it with real-time web search to synthesize a final, cited answer. This fulfills the requirements of Task A from the project brief.

Features
Structured Data Retrieval: Connects to a SQLite database to answer specific questions about projects and employees.

Unstructured Data Retrieval (RAG): Searches a FAISS vector database of internal documents to answer conceptual questions.

Real-time Web Search: Uses SerpAPI to find up-to-the-minute information on the web.

Explainability: The agent's thought process is printed to the console, showing which tool it chose and why for each query.

Project Setup and Installation
Follow these steps to set up and run the project locally.

Clone the Repository

git clone https://github.com/amanv13/Query-Resolution-AI-Agent.git
cd Query-Resolution-AI-Agent

Create and Activate Virtual Environment

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate

Install Dependencies

pip install -r requirements.txt

Set Up API Keys

Create a file named .env in the root of the project.

Add your API keys to the file in the following format:

GOOGLE_API_KEY="your_google_api_key_here"
SERPAPI_API_KEY="your_serpapi_key_here"

Prepare Data Sources

First, create and populate the SQL database:

python setup_database.py

Next, process the documents and create the vector index:

python ingest.py

How to Run the Agent
Once the setup is complete, you can start the agent with the following command:

python agent.py

The agent will launch and you can begin asking questions at the You: prompt. Type exit to quit.

Sample Queries & Outputs
Q1) Who is the lead for the project 'AI Agent Alpha'?

A) > Entering new AgentExecutor chain...

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

Invoking: `Employee_and_Project_Database_Search` with `Who is the lead for the project AI Agent Alpha?`

> Entering new SQL Agent Executor chain...

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

Invoking: `sql_db_list_tables` with `{}`

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

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

/*

3 rows from projects table:

project_id	project_name	status	lead_id

101	AI Agent Alpha	In Progress	2

102	Data Analytics Dashboard	Completed	1

103	Real-time Search Integration	Planning	2

*//opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

Invoking: `sql_db_query` with `{'query': "SELECT e.employee_name FROM employees e JOIN projects p ON e.id = p.lead_id WHERE p.project_name = 'AI Agent Alpha'"}`

Error: (sqlite3.OperationalError) no such column: e.employee_name

[SQL: SELECT e.employee_name FROM employees e JOIN projects p ON e.id = p.lead_id WHERE p.project_name = 'AI Agent Alpha']

(Background on this error at: https://sqlalche.me/e/20/e3q8)/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

Invoking: `sql_db_schema` with `{'table_names': 'employees'}`

responded: The query failed because the `employees` table does not have a column named `employee_name`. I will need to find the correct column name.

CREATE TABLE employees (

	id INTEGER, 

	name TEXT NOT NULL, 

	role TEXT NOT NULL, 

	start_date TEXT, 

	PRIMARY KEY (id)

)

/*

3 rows from employees table:

id	name	role	start_date

1	Alice	Data Scientist	2022-08-01

2	Bob	AI Engineer	2021-10-15

3	Charlie	Project Manager	2023-01-20

*//opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

Invoking: `sql_db_query` with `{'query': "SELECT e.name FROM employees e JOIN projects p ON e.id = p.lead_id WHERE p.project_name = 'AI Agent Alpha'"}`

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

[('Bob',)]Bob is the lead for the project AI Agent Alpha.

> Finished chain.

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

{'input': 'Who is the lead for the project AI Agent Alpha?', 'output': 'Bob is the lead for the project AI Agent Alpha.'}Bob is the lead for the project 'AI Agent Alpha'.

Q2) How many projects are in progress?

A) > Entering new AgentExecutor chain...

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

Invoking: `Employee_and_Project_Database_Search` with `How many projects are in progress?`

> Entering new SQL Agent Executor chain...

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

Invoking: `sql_db_list_tables` with `{}`

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

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

/*

3 rows from projects table:

project_id	project_name	status	lead_id

101	AI Agent Alpha	In Progress	2

102	Data Analytics Dashboard	Completed	1

103	Real-time Search Integration	Planning	2

*//opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

Invoking: `sql_db_query` with `{'query': "SELECT COUNT(*) FROM projects WHERE status = 'In Progress'"}`

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

[(1,)]There is 1 project in progress.

> Finished chain.

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

{'input': 'How many projects are in progress?', 'output': 'There is 1 project in progress.'}There is 1 project in progress.

Q3) What is the mission of the company?

A) > Entering new AgentExecutor chain...

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

Invoking: `Document_and_Policy_Search` with `company mission`

responded: I will need to search the company documents to answer this question.  I'll use the `Document_and_Policy_Search` tool.

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

[Document(id='bf9d05b2-de6e-43ec-b273-693ad6342f77', metadata={'source': 'docs/company_info.txt'}, page_content='Our mission is to democratize access to information through intelligent systems. We believe in open-source collaboration and ethical AI development. For support, please contact the AI engineering team.'), Document(id='998cfaba-3335-450f-af3e-53f310f99896', metadata={'source': 'docs/project_brief.txt'}, page_content='Project AI Agent Alpha is a high-priority initiative aiming to build a conversational agent for query resolution. The agent will leverage Retrieval-Augmented Generation (RAG) to pull from structured and unstructured data sources. The deadline is 3 days. Key technologies include LangChain and FAISS.')]Our mission is to democratize access to information through intelligent systems.  We believe in open-source collaboration and ethical AI development.

Q4) What are the key technologies for Project AI Agent Alpha?

A) > Entering new AgentExecutor chain...

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

Invoking: `Employee_and_Project_Database_Search` with `{'question': 'What are the key technologies for Project AI Agent Alpha?'}`

> Entering new SQL Agent Executor chain...

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

Invoking: `sql_db_list_tables` with `{}`

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

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

/*

3 rows from projects table:

project_id	project_name	status	lead_id

101	AI Agent Alpha	In Progress	2

102	Data Analytics Dashboard	Completed	1

103	Real-time Search Integration	Planning	2

*//opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

Invoking: `sql_db_query` with `{'query': "SELECT key_technologies FROM projects WHERE project_name = 'AI Agent Alpha'"}`

Error: (sqlite3.OperationalError) no such column: key_technologies

[SQL: SELECT key_technologies FROM projects WHERE project_name = 'AI Agent Alpha']

(Background on this error at: https://sqlalche.me/e/20/e3q8)/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

The query failed because the `key_technologies` column does not exist in the `projects` table.  I need to find a way to answer the question without that column.  I don't know.

> Finished chain.

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

{'input': 'What are the key technologies for Project AI Agent Alpha?', 'output': "The query failed because the `key_technologies` column does not exist in the `projects` table.  I need to find a way to answer the question without that column.  I don't know."}I am sorry, I was unable to find the key technologies for Project AI Agent Alpha in the available database.  The database search failed because the necessary information is not present.

Q5) What is the current time in Mumbai?

A) > Entering new AgentExecutor chain...

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

Invoking: `Web_Search` with `current time in Mumbai`

/opt/anaconda3/lib/python3.12/site-packages/langchain_google_genai/chat_models.py:357: UserWarning: Convert_system_message_to_human will be deprecated!

  warnings.warn("Convert_system_message_to_human will be deprecated!")

9:53 PMThe current time in Mumbai is 9:53 PM.

Q6) Who won the last cricket world cup?

A) Agent: Australia won the last Cricket World Cup.
