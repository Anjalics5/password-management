import random
import string

def check_strength(password):
    strength = 0
    
    if len(password) >= 8:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):p
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    if strength == 4:
        return "Strong "
    elif strength == 3:
        return "Medium "
    else:
        return "Weak "

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(10))
    return password

# User input
user_password = input("Enter your password: ")
print("Strength:", check_strength(user_password))

print("Suggested Strong Password:", generate_password())
