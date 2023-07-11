import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def encrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path, key)

def main_encrypto():
    key = Fernet.generate_key()
    encrypt_directory('cripto_folder', key)
    print(key)

    return key
