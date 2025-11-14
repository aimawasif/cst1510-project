import bcrypt

def hash_password(plain_text_pass):
    pass_bytes = plain_text_pass.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(pass_bytes, salt)
    return hashed_pass.decode('utf-8')   # ✅ Return string, easier to store in file



#This is how bcrypt checks passwords correctly.
def verify_password(plain_text_pass, stored_hash):
    return bcrypt.checkpw(
        plain_text_pass.encode('utf-8'),
        stored_hash.encode('utf-8')
    )


#creating .txt empty file
import os

def ensure_user_file():
    if not os.path.exists("users.txt"):
        with open("users.txt", "w", encoding="utf-8") as f:
            pass



def retrieve_pass_hash(username):
    with open("users.txt", "r") as f:
        for line in f:
            stored_user, stored_hash = line.strip().split(",")
            if stored_user == username:
                return stored_hash
    return None


#create the login function:
def user_exists(username):
    """Check if a username already exists in users.txt"""
    if not os.path.exists("users.txt"):
        return False
    with open("users.txt", "r", encoding="utf-8") as f:
        for line in f:
            stored_user, _ = line.strip().split(",")
            if stored_user == username:
                return True
    return False


def register_user(username, password):
    """Register a new user by hashing their password and saving it."""
    ensure_user_file()

    if user_exists(username):
        print(f"Error: Username '{username}' already exists.")
        return False

    hashed = hash_password(password)

    with open("users.txt", "a", encoding="utf-8") as f:
        f.write(f"{username},{hashed}\n")

    print(f"Success: User '{username}' registered successfully!")
    return True

def login_user(username, password):
    """Authenticate user by verifying username and password."""
    if not os.path.exists("users.txt"):
        print("No users registered yet.")
        return False

    stored_hash = retrieve_pass_hash(username)
    if stored_hash is None:
        print("Error: Username not found.")
        return False

    if verify_password(password, stored_hash):
        print(f"Success: Welcome, {username}!")
        return True
    else:
        print("Error: Invalid password.")
        return False

  
def main():
    print("\nWelcome to the Secure Authentication System!")

    while True:
        print("\n[1] Register")
        print("[2] Login")
        print("[3] Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            register_user(username, password)

        elif choice == "2":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            login_user(username, password)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    ensure_user_file()
    main()

      
      

