import os
from cryptography.fernet import Fernet

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def decrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            decrypt_file(file_path, key)

def main_decrypto(key):
    # key = b'your_private_key_here'
    decrypt_directory('cripto_folder', key)