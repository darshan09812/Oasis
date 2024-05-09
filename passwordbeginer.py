import random
import string

# Beginner Version: Command-Line Password Generator

def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter password length: "))
        include_letters = input("Include letters? (yes/no): ").lower() == 'yes'
        include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
        
        password = generate_password(length, include_letters, include_numbers, include_symbols)
        print("Generated Password:", password)
        
    except ValueError:
        print("Please enter a valid password length.")

if __name__ == "__main__":
    main()
