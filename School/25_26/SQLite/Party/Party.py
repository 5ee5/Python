import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "party.db")

def create_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS parties (
            party_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS guests (
            guest_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            party_id INTEGER NOT NULL,
            FOREIGN KEY(party_id) REFERENCES parties(party_id)
        )
    """)

    conn.commit()
    conn.close()


def add_party(name, date):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO parties (name, date) VALUES (?, ?)", (name, date))
    conn.commit()
    conn.close()
    print(f"Added party '{name}' on {date}.")


def list_parties():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM parties")
    rows = c.fetchall()
    conn.close()

    if not rows:
        print("\nNo parties found.")
        return

    print("\n--- Parties ---")
    print(f"{'ID':<4} {'Name':<30} {'Date':<15}")
    print("-" * 50)
    for pid, name, date in rows:
        print(f"{pid:<4} {name:<30} {date:<15}")


def delete_party(pid):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("DELETE FROM guests WHERE party_id = ?", (pid,))
    c.execute("DELETE FROM parties WHERE party_id = ?", (pid,))
    
    conn.commit()
    conn.close()
    print(f"Party {pid} deleted.")


def add_guest(name, party_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("INSERT INTO guests (name, party_id) VALUES (?, ?)", (name, party_id))
    conn.commit()
    conn.close()
    print(f"Added guest '{name}' to party {party_id}.")


def list_guests():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        SELECT guests.guest_id, guests.name, parties.name
        FROM guests
        JOIN parties ON guests.party_id = parties.party_id
    """)
    rows = c.fetchall()
    conn.close()

    if not rows:
        print("\nNo guests found.")
        return

    print("\n--- Guests (All Parties) ---")
    print(f"{'ID':<4} {'Guest Name':<25} {'Party':<25}")
    print("-" * 60)
    for gid, gname, pname in rows:
        print(f"{gid:<4} {gname:<25} {pname:<25}")


def list_guests_for_party(pid):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT name FROM guests WHERE party_id = ?", (pid,))
    guests = c.fetchall()
    conn.close()

    if not guests:
        print("\nNo guests for this party.")
        return

    print(f"\n--- Guests for Party {pid} ---")
    for (name,) in guests:
        print(f"- {name}")


def delete_guest(gid):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM guests WHERE guest_id = ?", (gid,))
    conn.commit()
    conn.close()
    print(f"Guest {gid} deleted.")



create_db()

while True:
    print("\n--- Party Manager ---")
    print("1 - Add party")
    print("2 - List parties")
    print("3 - Delete party")
    print("4 - Add guest")
    print("5 - List guests")
    print("6 - List guests for party")
    print("7 - Delete guest")
    print("exit - Quit")
    choice = input("Select action: ")

    if choice == "1":
        name = input("Party name: ")
        date = input("Party date (YYYY-MM-DD): ")
        add_party(name, date)

    elif choice == "2":
        list_parties()

    elif choice == "3":
        pid = input("Party ID to delete: ")
        delete_party(pid)

    elif choice == "4":
        list_parties()
        pid = input("Party ID to add guest to: ")
        gname = input("Guest name: ")
        add_guest(gname, pid)

    elif choice == "5":
        list_guests()

    elif choice == "6":
        pid = input("Party ID: ")
        list_guests_for_party(pid)

    elif choice == "7":
        gid = input("Guest ID to delete: ")
        delete_guest(gid)

    elif choice in ("exit", "quit"):
        quit()

    else:
        print("Invalid choice.")
