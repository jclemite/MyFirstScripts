#hashing files for Kali Linux
#first try - 10/05/18


import hashlib

inputFile = input("hashpractice1.txt:")
openedFile = open(inputFile)
readFile = openedFile.read()

md5Hash = hashlib.md5(readFile)
md5Hashed = md5Hash.hexdigest()

sha1Hash = hashlib.sha1(readFile)
sha1Hashed = sha1Hash.hexdigest()


print (("File Name: %s") % inputFile)
print (("MD5: %r") % md5Hashed)
print (("SHA1: %r") % sha1Hashed) 
