# Developed by hamed pariazar
from cryptography.fernet import Fernet
import hashlib
import os.path

def getPattern(fileName):
    pattern = abs(hash(fileName)) % (10 ** 8)
    return(pattern+1)

def load_key(fileName):
    """
    Loads the key from the current directory named `key.key`
    """
    return open("Key\\"+fileName+"_"+"key.key", "rb").read()

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


#Decrypt Algorithm DAES
path="data"
for path,subdir,files in os.walk(path):
   for name in files:  
        #write_key(name)
        #write_key()

        key = load_key(name)
        print('data: ' + os.path.join(path,name))
        print('Key: '+ str(key))
        for x in range(2):            
            decrypt(os.path.join(path,name),key)