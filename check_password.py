from getpass import getpass
import hashlib
import requests

def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5 = sha1_password[:5]
    tail = sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{first5}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error connecting to the API.")
        return 0

    hashes = (line.split(':') for line in response.text.splitlines())

    for h, count in hashes:
        if h == tail:
            return int(count)

    return 0


password = getpass("Enter the password to test: ")
count = pwned_api_check(password)

if count:
    print(f"⚠️ This password has appeared {count} times in data breaches.")
    print("❌ Do not use this password.")
else:
    print("✅ This password was not found in known breaches.")
    print("🔐 Make sure it is still long and unique.")