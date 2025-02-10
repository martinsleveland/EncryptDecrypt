from cryptography.fernet import Fernet
import os

# Generate or load encryption key
def generate_or_load_key():
    """Generate a new encryption key if it doesn't exist, otherwise load the existing one."""
    key_file = "secret.key"
    if os.path.exists(key_file):
        with open(key_file, "rb") as file:
            key = file.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, "wb") as file:
            file.write(key)
    return key

# Encrypt message
def encrypt_message(message, key):
    """Encrypt a given message using Fernet encryption."""
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

# Load or generate key
key = generate_or_load_key()

# Get user input
message = input("Enter the message you want to encrypt: ")
file_name = input("Enter the filename to save the encrypted message (e.g., secret_message.txt): ")

# Encrypt the message
encrypted_msg = encrypt_message(message, key)

# Save the encrypted message to the specified file
with open(file_name, "wb") as file:
    file.write(encrypted_msg)

print(f"\n🔹 Encrypted Message saved to '{file_name}'")
print(f"🔑 Encryption Key (Keep this secret!): {key.decode()}")
