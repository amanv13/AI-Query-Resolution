import sqlite3

conn = sqlite3.connect('company_data.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    start_date TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL,
    status TEXT,
    lead_id INTEGER,
    FOREIGN KEY (lead_id) REFERENCES employees (id)
)
''')

cursor.execute("INSERT INTO employees (id, name, role, start_date) VALUES (1, 'Alice', 'Data Scientist', '2022-08-01')")
cursor.execute("INSERT INTO employees (id, name, role, start_date) VALUES (2, 'Bob', 'AI Engineer', '2021-10-15')")
cursor.execute("INSERT INTO employees (id, name, role, start_date) VALUES (3, 'Charlie', 'Project Manager', '2023-01-20')")

cursor.execute("INSERT INTO projects (project_id, project_name, status, lead_id) VALUES (101, 'AI Agent Alpha', 'In Progress', 2)")
cursor.execute("INSERT INTO projects (project_id, project_name, status, lead_id) VALUES (102, 'Data Analytics Dashboard', 'Completed', 1)")
cursor.execute("INSERT INTO projects (project_id, project_name, status, lead_id) VALUES (103, 'Real-time Search Integration', 'Planning', 2)")

conn.commit()
conn.close()

print("Database 'company_data.db' created and populated successfully.")