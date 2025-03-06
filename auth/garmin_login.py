import garth
from getpass import getpass

email = input("Enter email: ")
password = getpass("Enter password: ")

def login_to_garmin():
    email = input("Enter email: ")
    password = getpass("Enter password: ")

    try:
        garth.login(email, password)
        print("Login successful!")
        # Save the session tokens
        garth.save("~/.garth")
    except Exception as e:
        print(f"Login failed: {e}")