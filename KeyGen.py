from cryptography.fernet import Fernet
import os.path
#Key Generator
import os.path

def createKeis():
    for root, dirs, files in os.walk("data"):
        for filename in files:
            key = Fernet.generate_key()
            with open("Key\\"+filename+"_"+"key.key", "wb") as key_file:
                key_file.write(key)
    print('all keys created!')