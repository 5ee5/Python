import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "support.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        type TEXT NOT NULL,
        topic TEXT NOT NULL,
        description TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        status TEXT NOT NULL
    );
    """)

    conn.commit()
    conn.close()
    print("Table 'tickets' created successfully!")

def insert_ticket(user_id, ticket_type, topic, description, status):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tickets (user_id, type, topic, description, status)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, ticket_type, topic, description, status))

    conn.commit()
    conn.close()
    print("Ticket inserted successfully!")

def fetch_all_tickets():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets")
    rows = cursor.fetchall()

    conn.close()
    return rows

init_db()

#insert_ticket(100, 'Bug', 'Bug_Report', 'Nothing happens when I click the button.', 'open')
tickets = fetch_all_tickets()
print(tickets)