#URL = input(str("The URL is:"))
#print("Our url is:", URL)

#Ip = input(str("Our IP address is:"))

#print(Ip)

# create two variables. one for user name and the other for neighbor name
userName = input(str("What is your first name?"))
neighborName = input(str("What is your neighbor's first name?"))

# create two more variables for how long youve been coding and the same for neighbor

monthsCoded = int(input("How many months have you been coding?"))
monthsneighborCoded = int(input("How many months has your neighbor been coding?"))

# create a variable to combine how many months you all have been coding for

monthsweCoded =  monthsCoded + monthsneighborCoded

# print statements. first saying "I am ____  and my neighbor is ___". second will say "Together we have coded for ____"

print("I am", userName, "and my neighbor is", neighborName)
print("Together we have been coding for", monthsweCoded)