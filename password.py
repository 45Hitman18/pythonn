import random
import string

def generate_password(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

length = int(input("Enter the password length: "))
print("Generated Password:", generate_password(length))
