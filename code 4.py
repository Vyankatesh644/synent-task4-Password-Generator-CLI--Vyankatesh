import random
import string

print("=== Password Generator ===")

# Take password length from user
length = int(input("Enter password length: "))

# Character combinations
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
special_chars = string.punctuation

# Combine all characters
all_characters = uppercase + lowercase + numbers + special_chars

# Generate password
password = ""

for i in range(length):
    password += random.choice(all_characters)

# Display password
print("Generated Password:", password)