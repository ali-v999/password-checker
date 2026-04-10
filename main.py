import re
import random
import string

# Common weak passwords
common_passwords = ["123456", "password", "qwerty", "111111", "abc123"]

def check_password(password):
    score = 0

    if password in common_passwords:
        return "Very Weak Password ❌ (common password)"

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 1

    if score <= 2:
        return "Weak Password ❌"
    elif score == 3 or score == 4:
        return "Medium Password ⚠️"
    elif score == 8:
        return "Strong Password ✅"
    else:
        return "Very Strong Password 🔥"


# Password generator
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(characters) for i in range(length))
    return password


# Menu system
print("1. Check Password")
print("2. Generate Password")

choice = input("Choose option (1/2): ")

if choice == "1":
    password = input("Enter password: ")
    print(check_password(password))

elif choice == "2":
    length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(length))

else:
    print("Invalid choice ❌")
