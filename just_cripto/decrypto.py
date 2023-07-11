from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64

def decrypt_file(filename, private_key):
    # Read the encrypted file
    with open(filename, 'rb') as encrypted_file:
        encrypted_key = encrypted_file.read(256)
        encrypted_data = encrypted_file.read()

    # Decrypt the symmetric key using the private key
    symmetric_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Decrypt the data using the symmetric key
    decrypted_data = decrypt_data(encrypted_data, symmetric_key)

    # Save the decrypted data to a new file
    with open(filename + '.decrypted', 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

def decrypt_data(data, key):
    # Decrypt the data using the symmetric key
    cipher_suite = Fernet(base64.urlsafe_b64encode(key))
    decrypted_data = cipher_suite.decrypt(data)
    return decrypted_data

def main_decrypto():

    private_key = input('Please paste the private_key file in root directory and than press enter', )

    # Load the private key from file
    with open('private_key.pem', 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )   

    # Decrypt the file
    file_to_decrypt = '1203105290_202307031722_ok5.pdf.encrypted'
    decrypt_file(file_to_decrypt, private_key)

    print(f'File "{file_to_decrypt}" successfully decrypted. Decrypted data saved to "{file_to_decrypt}.decrypted".')
