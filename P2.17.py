#Jordan Lemite
#P2.17
#CSMC 140-2
#13 Sep 2017

#military time, compute interval

# 0800 1215 -> "4 hours 15 minutes"
# 0900 1000 -> "1 hours 0 minutes" (no special cases
# 1745 2015 -> "2 hours 30 minutes" (wrap minutes
# 1730 0300 -> "9 hours 30 minutes" (wrap hours ar

#read in the time

firstTime = int(input("First time: "))
secondTime =  int(input("Second time: "))

print(firstTime, secondTime)
#print(secondTime - firstTime)

#seperate hours, minutes
firsthour = firstTime // 100
firstminute = firstTime % 100

print(firsthour, firstminute)
