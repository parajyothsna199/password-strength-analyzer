
import re

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 2
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[!@#$%^&*]", password):
        score += 2

    if score <= 3:
        return "Weak ❌"
    elif score <= 6:
        return "Medium ⚠️"
    else:
        return "Strong ✅"

pwd = input("Enter password: ")
print(check_password(pwd))
