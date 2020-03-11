# Import the module that stores string data
import string

# Collect and print out all ascii letters - lowercase and uppercase
result = string.ascii_letters
print(result)
# Collect and print out all of the numeric digits
result2 = string.digits
print(result2)
######################

# Import the module that can generate random numbers
import random
# Collect and print out a random integer between 1 and 10
result3 = random.randint(1, 10)
print(result3)
# Randomly shuffle the below list and print it to the terminal
listOfValues = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(listOfValues)
print(listOfValues)
######################

# Import the module used for hashing messages
import hashlib
# Collect and print out all of the available hashing algorithms
result4 = hashlib.algorithms_available
print(result4)