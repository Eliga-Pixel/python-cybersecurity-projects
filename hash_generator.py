import hashlib

def generate_hashes(text):
    print("\n🔐 Hash Results")
    print("=" * 60)

    # MD5
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    print(f"MD5     : {md5_hash}")

    # SHA-1
    sha1_hash = hashlib.sha1(text.encode()).hexdigest()
    print(f"SHA-1   : {sha1_hash}")

    # SHA-256
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    print(f"SHA-256 : {sha256_hash}")

    # SHA-512
    sha512_hash = hashlib.sha512(text.encode()).hexdigest()
    print(f"SHA-512 : {sha512_hash}")

# Ask the user for text
text = input("Enter text to hash: ")

# Generate hashes
generate_hashes(text)