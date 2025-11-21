import sqlite3

def create_db():
    """Creates the database and parties table if they don't exist."""
    conn = sqlite3.connect('party.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS parties (
            party_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_party(name, date):
    """Adds a party to the database and confirms success."""
    conn = sqlite3.connect('party.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO parties (name, date) VALUES (?, ?)", (name, date))
        conn.commit()
        print(f"Success: Party '{name}' on {date} has been added to the database.")
    except sqlite3.Error as e:
        print(f"Error adding party: {e}")
    finally:
        conn.close()

create_db()

while True:
    print("\n--- Party Manager ---")
    print("1 - Add party")
    print("2 - Add guest")
    print("exit - Quit the app")
    choice = input("Select action: ")

    if choice == "1":
        p_name = input("Enter Party Name: ")
        p_date = input("Enter Party Date (e.g., YYYY-MM-DD): ")
        add_party(p_name, p_date)
        
    elif choice == "2":
        # adding guest (Placeholder as per original code)
        print("Feature not implemented yet.")
        pass
        
    elif choice == "exit" or "quit":
        quit()
        
    else:
        print("Unrecognized command")