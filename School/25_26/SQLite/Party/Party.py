import sqlite3

while True:
    print("1. Add party")
    print("2. Add guest")
    print("exit/quit - Quit the App")
    choice = input("Select action: ")

    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "exit" or "quit":
        quit()
    else:
        print("Invalid choice")