import hashlib
import os


def calculate_sha256(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            sha256.update(chunk)

    return sha256.hexdigest()


def save_hash(filename, file_hash):
    hash_file = filename + ".sha256"

    with open(hash_file, "w") as f:
        f.write(file_hash)

    print(f"💾 Hash saved to: {hash_file}")


def verify_hash(filename, current_hash):
    hash_file = filename + ".sha256"

    if not os.path.exists(hash_file):
        print("⚠️ No saved hash found.")
        return

    with open(hash_file, "r") as f:
        saved_hash = f.read().strip()

    if saved_hash == current_hash:
        print("✅ File integrity verified. No changes detected.")
    else:
        print("🚨 WARNING: File has been modified!")


def main():
    filename = input("Enter the path to the file: ")

    if not os.path.exists(filename):
        print("❌ File not found.")
        return

    print("🔍 Calculating SHA-256 hash...")
    current_hash = calculate_sha256(filename)

    print("\nSHA-256 Hash:")
    print(current_hash)

    choice = input("\nDo you want to (s)ave or (v)erify? ").lower()

    if choice == "s":
        save_hash(filename, current_hash)
    elif choice == "v":
        verify_hash(filename, current_hash)
    else:
        print("❌ Invalid choice.")


if __name__ == "__main__":
    main()