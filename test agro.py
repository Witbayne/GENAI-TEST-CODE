import json
from abc import ABC, abstractmethod

# Abstract USSD Interface
class USSDInterface(ABC):
    @abstractmethod
    def display_menu(self):
        pass

# User base class
class User(ABC):
    def __init__(self, name, phone, pin):
        self.name = name
        self.phone = phone
        self.pin = pin

    @abstractmethod
    def user_type(self):
        pass

# Farmer and Buyer classes inherit User
class Farmer(User):
    def user_type(self):
        return "Farmer"

class Buyer(User):
    def user_type(self):
        return "Buyer"

# Main USSD Menu
class MainMenu(USSDInterface):
    def display_menu(self):
        print("\nWelcome to AgroUSSD")
        print("Dial USSD code *752* to access the system.")

# Simple file-based user storage
USER_FILE = "users.json"

def load_users():
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

def sign_up():
    print("\n--- Sign Up ---")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    pin = input("Set a 4-digit PIN: ")
    role = input("Are you a Farmer or Buyer? (F/B): ").strip().upper()
    if role == "F":
        user = Farmer(name, phone, pin)
    elif role == "B":
        user = Buyer(name, phone, pin)
    else:
        print("Invalid role selected.")
        return

    users = load_users()
    if phone in users:
        print("User already exists. Please login.")
        return
    users[phone] = {
        "name": user.name,
        "pin": user.pin,
        "role": user.user_type()
    }
    save_users(users)
    print(f"Sign up successful! Welcome, {user.name} ({user.user_type()})")

def login():
    print("\n--- Login ---")
    phone = input("Enter your phone number: ")
    pin = input("Enter your 4-digit PIN: ")
    users = load_users()
    user = users.get(phone)
    # Only allow access if PIN matches
    if user and user["pin"] == pin:
        print(f"Login successful! Welcome back, {user['name']} ({user['role']})")
        # Here you would call FarmerMenu or BuyerMenu based on user['role']
    else:
        print("Invalid phone or PIN.")

def main():
    menu = MainMenu()
    while True:
        menu.display_menu()
        ussd = input("Enter USSD code to continue or 'exit' to quit: ")
        if ussd == "*752*":
            print("\n1. Sign Up\n2. Login\n3. Exit")
            choice = input("Select option: ")
            if choice == "1":
                sign_up()
            elif choice == "2":
                login()
            elif choice == "3":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
        elif ussd.lower() == "exit":
            print("Exiting AgroUSSD. Goodbye!")
            break
        else:
            print("Invalid USSD code. Please dial *752* to access.")

main()