# create variable in string form of URL and IP address
URL = "www.AlpacasRUS.edu"
IP = "192.168.1.12"
print(URL)
print(IP)

# create a variable for each weekday using ints and how many hits they got on that day
Monday = 3
Tuesday = 40
Wednesday = 93
Thursday = 0
Friday = 16
Saturday = 111
Sunday = 31

print(Monday)
print(Tuesday)
print(Wednesday)
print(Thursday)
print(Friday)
print(Saturday)
print(Sunday)

#create a variable adding all the hits from the week together
#Create a variable which takes weeklyHits and divides it by numofDays

weeklyHits = int(Monday) + int(Tuesday) + int(Wednesday) + int(Thursday) + int(Friday) + int(Saturday) + int(Sunday)
#weeklyHits = sum(week)
numofDays= 7
avgHits = weeklyHits / numofDays

print(weeklyHits)
print(avgHits)