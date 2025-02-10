from cryptography.fernet import Fernet

# Load key
def load_key():
    """Load the previously generated encryption key from the secret.key file."""
    try:
        with open("secret.key", "rb") as file:
            return file.read()
    except FileNotFoundError:
        print("❌ Error: secret.key file not found! You need the correct key to decrypt.")
        exit()

# Decrypt message
def decrypt_message(encrypted_message, key):
    """Decrypt the given encrypted message using Fernet encryption."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()

# Ask user for the filename
file_name = input("Enter the name of the encrypted file (e.g., encrypted_message.txt): ")

# Try to read the encrypted file
try:
    with open(file_name, "rb") as file:
        encrypted_msg = file.read()
except FileNotFoundError:
    print(f"❌ Error: The file '{file_name}' was not found!")
    exit()

# Load key and attempt decryption
key = load_key()
try:
    decrypted_msg = decrypt_message(encrypted_msg, key)
    print(f"🔹 Decrypted Message: {decrypted_msg}")
except Exception:
    print("❌ Error: Unable to decrypt! Invalid key or message corruption.")
