#Jordan Lemite
#CSMC 140-2
#p3.12

grade = input("letter: ")

if grade[0] == "A" : 
    score = 4.0

elif grade[0] == "B" :
    score = 3.0

elif grade[0] == "C" :
    score = 2.0

elif grade[0] == "D" :
    score = 1.0

elif grade[0] == "F" :
    score = 0

if grade[1] == "+" :
    score = score + 0.3

elif grade[1] == "-" :
    score = score - 0.3

if grade == "A+" :
    score = 4.0

elif grade == "F+" :
    score = 0

elif grade == "F-" :
    score = 0



print(score)

    
    
