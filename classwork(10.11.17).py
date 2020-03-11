# list from nums
# 11 Oct 2017
# Jordan Lemite

# reads two ints, makes and prints list of nums
# between them (inclusive) 
# 5 9 -> [5, 6, 7, 8, 9]

first = int(input("First num: "))
second = int(input("Second num: ")) 

# init:
result = []
i = first

# loop:
if first < second :
    while i <= second   :
        result.append(i) 
        i = i + 1 
else :
    while i >= second :
        result.append(i)
        i = i - 1
# print result:
print ( result ) 
