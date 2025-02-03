import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import hashlib

# Decrypt the data using AES
def decrypt_data(ciphertext, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=b'1234567890abcdef')  # 16-byte IV for CBC mode
    decrypted = unpad(cipher.decrypt(base64.b64decode(ciphertext)), AES.block_size)
    return decrypted.decode()

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))  # Listen on localhost:9999
server.listen(5)

print("Server is waiting for connection...")

while True:
    client_socket, addr = server.accept()
    print(f"Connection established with {addr}")

    data = client_socket.recv(1024).decode()
    if data:
        print(f"Encrypted data received: {data}")
        key = hashlib.sha256(b"my_secret_key").digest()  # Ensure key length is 32 bytes
        decrypted_data = decrypt_data(data, key)
        print(f"Decrypted data: {decrypted_data}")
    
    client_socket.close()
