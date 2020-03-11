# Pull in the CSV file and store it to file
#file = open("UserList.csv")
import csv
csvFile = open("UserList.csv")
# Read the file to convert it into text to store in contents
#contents = file.read()
reader = csv.reader(csvFile)
# reference the file to place the user summaries into
userSummary =  open("PeopleToKeepEyesOn.txt", "w")

# Split the contents into a list of rows based on the newline
#rows = contents.split("\n"

# Loop through the rows in order to find which ones contain "229.62.232.190"
for row in reader:

    # Split the IPs columns on semis
    #user_info = row.split(",")
    ipList = row[3].split(";")

    # If the index of "229.62.232.190" is found then print "COMPANY SERVER FOUND" and user info
    if"229.62.232.190" in ipList:
        userSummary.write("COMPANY PRIVATE SERVER FOUND\n")

        # Print out the user's name, password, and hours online
        userSummary.write("USER: " + row[0] + '\n')
        userSummary.write("PASSWORD: " + row[1])
        userSummary.write("HOURS ONLINE: " + user_info[2])

        # Split the IP column into a list on semicolons
        ip_list = user_info[3].split(";")

        # Loop through the ip_list and print them to the screen
        print("IPs:")
        for IP in ip_list:
            print(IP)

        print("----------")


file.close()