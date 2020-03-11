# hashing files for Kali Linux
# second try - 10/05/18

import hashlib

hasher = hashlib.md5()
with open('hashpractice1.txt', 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
print (hasher.hexdigest())



# SUCCESSSSSS!!!!
