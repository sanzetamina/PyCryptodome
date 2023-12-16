from dotenv import load_dotenv
import os
from Crypto.Cipher import AES
import binascii

# Load environment variables from a .env file
load_dotenv("config.env")

# Accessing environment variables
plain_text = os.getenv("PLAIN_TEXT", "default_plain_text")
key_hex = os.getenv("KEY_HEX", "default_key_hex")


# Function to pad the plaintext to be a multiple of 16 bytes
def pad(text):
    while len(text) % 16 != 0:
        text += " "  # Padding with spaces
    return text


# Pad the plaintext
padded_text = pad(plain_text).encode()

# Convert the key from hex to bytes
key_bytes = bytes.fromhex(key_hex)

# Create an AES cipher object
cipher = AES.new(key_bytes, AES.MODE_ECB)

# Encrypt the plaintext
encrypted_bytes = cipher.encrypt(padded_text)

# Convert the encrypted bytes to a hexadecimal string
encrypted_hex = binascii.hexlify(encrypted_bytes).decode("utf-8")

# Convert to uppercase if needed
encrypted_hex_upper = encrypted_hex.upper()

# Output the result
print(encrypted_hex_upper)
