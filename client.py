import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import hashlib

# Encrypt the data using AES
def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=b'1234567890abcdef')  # 16-byte IV for CBC mode
    padded_data = pad(data.encode(), AES.block_size)
    encrypted = cipher.encrypt(padded_data)
    return base64.b64encode(encrypted).decode()

# Set up the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))  # Connect to the server on localhost:9999

message = input("Enter the message to send to the server: ")
key = hashlib.sha256(b"my_secret_key").digest()  # Ensure key length is 32 bytes
encrypted_message = encrypt_data(message, key)

print(f"Encrypted message: {encrypted_message}")

client.send(encrypted_message.encode())
client.close()
