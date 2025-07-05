import random
import string

def generate_password(length):
    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")

    # Character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Ensure password has at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special),
    ]

    # Fill the rest with random characters from all combined
    all_chars = uppercase + lowercase + digits + special
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the result
    random.shuffle(password)
    return ''.join(password)

# CLI
if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length: "))
        print("Generated Password:", generate_password(length))
    except ValueError as ve:
        print("Error:", ve)
