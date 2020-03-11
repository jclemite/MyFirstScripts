#MD5 hashing for passwords
#10.11.18


import hashlib

password= "Apple07"
hash_password = hashlib.md5(password.encode())
print(hash_password.hexdigest())

