import encrypto 
import decrypto
import random
import string
import time

def generate_key():
    # string.punctuation
    symbols = ''.join(['@', '#', '?', '*', '&'])
    key = ''.join(random.choices(symbols + string.ascii_uppercase + string.digits + string.ascii_lowercase, k=31))
    return key

def main():
    # list_randomKey = []

    # for _ in range(10):
    #     random_key = generate_key()
    #     list_randomKey.append(random_key)

    # with open('req.txt', 'w') as f:
    #     f.write('\n'.join(list_randomKey))

    # print(list_randomKey)
    # time.sleep(7)
    encrypto.main_encrypto()
    decrypto.main_decrypto()

if __name__=="__main__":
    main()

