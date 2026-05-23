# Biometric Authentication System (Final Step)

import time

print("=== BIOMETRIC AUTHENTICATION SYSTEM ===\n")

# Sample database
user_db = {
    "user1": {
        "pin": "1234",
        "fingerprint": "ABC123"
    }
}

# LOGIN
username = input("Enter username: ")

if username in user_db:

    pin = input("Enter PIN: ")

    if pin == user_db[username]["pin"]:
        print("\nPIN verified ✔️")
        print("Scanning fingerprint...")
        time.sleep(2)

        # BIOMETRIC CHECK
        fingerprint = input("Place finger (enter fingerprint ID): ")

        if fingerprint == user_db[username]["fingerprint"]:
            print("\nAuthentication Successful ✅")
            print("Access Granted 🔓")
        else:
            print("\nFingerprint mismatch ❌")
            print("Access Denied 🔒")

    else:
        print("Incorrect PIN ❌")

else:
    print("User not found ❌")