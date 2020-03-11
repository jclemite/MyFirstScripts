#Jordan Lemite
#P4.5
#October 30th, 2017
#CSMC 140-02
#Write a program that reads a set of floating point values
#Ask the user to enter the values, then print
#the average, the smallest, the largest, the range(largest minus smallest)

line = float(input("Type a num or blank to end: "))
numlist = []

while line != "":
    num = float(line)
    numlist.append(num)
    line = input("Type a num or blank to end: ")

total = 0.0
for num in numlist:
    total = total + num
    howmany = len(numlist)
    avg = total / howmany

print("the average",avg)

largest = numlist[0]
for num in numlist:
    if num > largest:
        largest = num 

print("the largest", largest)

smallest = numlist[0]
for num in numlist:
    if num < smallest:
        smallest = num 

print("the smallest", smallest)

for num in numlist:
    the_range = largest - smallest

print("the range", the_range)
    
