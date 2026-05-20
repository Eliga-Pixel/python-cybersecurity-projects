import re
from getpass import getpass

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 12:
        score += 1

    # Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1

    # Special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    # Display results
    print("\nPassword Analysis:")
    print(f"Length: {len(password)} characters")

    # Rating
    if score <= 2:
        print("❌ Strength: Weak")
    elif score <= 4:
        print("⚠️ Strength: Medium")
    else:
        print("✅ Strength: Strong")


# Ask user for password securely
password = getpass("Enter a password to analyze: ")

# Analyze the password
check_password_strength(password)