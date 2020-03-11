#Jordan Lemite
#CSMC 140-2
#p3.16


string1 = input("word: ")
string2 = input("word: ")
string3 = input("word: ")

if string1 >= string2 and string2 >= string3 :
    print(string1,string2,string3)
elif string2 < string1 :
    print(string2,string1)
elif string3 > string2 :
    print(string3,string2)
elif string1 > string3 and string3 > string2 :
    print(string1,string3,string2)
elif string1 >= string2 and string1 >= string3 and string2 > string3 :
    print(string1,string2,string3)
elif string1 > string2 and string2 > string3 and string1 > string3 :
    print(string1,string2,string3)
else:
    if string1 >= string2 and string2 >= string3 :
        print(string1,string2,string3)
    elif string2 < string1 :
        print(string2,string1)
    elif string3 > string2 :
        print(string3,string2)
    elif string1 > string3 and string3 > string2 :
        print(string1,string3,string2)
    elif string1 >= string2 and string1 >= string3 and string2 > string3 :
        print(string1,string2,string3)
    elif string1 > string2 and string2 > string3 and string1 > string3:
        print(string1,string2,string3)
    
o = 4
p = 2 + 2
if o == p:
    o - 1
    print("quick Maths")
