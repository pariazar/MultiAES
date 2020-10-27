#Encrypt Algorithm DAES
import os.path
from cryptography.fernet import Fernet
import hashlib
import KeyGen

def getPattern(fileName):
    pattern = abs(hash(fileName)) % (10 ** 8)
    return(pattern+1)

def load_key(fileName):
    """
    Loads the key from the current directory named `key.key`
    """
    return open("Key\\"+fileName+"_"+"key.key", "rb").read()


def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
         # encrypt data
        encrypted_data = f.encrypt(file_data)
        # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)


KeyGen.createKeis()

path="data"
for path,subdir,files in os.walk(path):
   for name in files:  
        #write_key()
        key = load_key(name)
        print('data: ' + os.path.join(path,name))
        print('Key: '+ str(key))
        for x in range(2):
            #print(x)
            encrypt(os.path.join(path,name),key)
      