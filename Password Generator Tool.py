import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, numbers=True, symbols=True):
    """
    Generate a random password based on user preferences.

    Parameters:
    - length: Length of the password (default is 12).
    - uppercase: Include uppercase letters (default is True).
    - lowercase: Include lowercase letters (default is True).
    - numbers: Include numbers (default is True).
    - symbols: Include symbols (default is True).

    """
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        print("Error: Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator Tool")

    length = int(input("Enter the length of the password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    generated_password = generate_password(length, uppercase, lowercase, numbers, symbols)

    if generated_password:
        print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()
