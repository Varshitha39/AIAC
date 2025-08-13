
# Function to register a new user by storing username and password in a dictionary
def register_user(users_db):
    """
    Registers a new user by asking for a username and password.
    Stores the credentials in the users_db dictionary.
    """
    username = input("Enter a new username: ")
    if username in users_db:
        print("Username already exists. Please try a different username.")
        return
    password = input("Enter a new password: ")
    users_db[username] = password
    print("Registration successful!")

# Function to log in a user by verifying username and password
def login_user(users_db):
    """
    Logs in a user by asking for username and password.
    Checks the credentials against the users_db dictionary.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users_db and users_db[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Example usage
if __name__ == "__main__":
    users_db = {}
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_user(users_db)
        elif choice == "2":
            login_user(users_db)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")



