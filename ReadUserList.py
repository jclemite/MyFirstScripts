# Pull in the CSV file and store it to file
csvfile = open("UserList.csv", "r")
# Read the file to convert it into text to store in contents

csvtext = csvfile.read()

# Split the contents into a list of rows based on the newline
csvtext.split("\n")

# Loop through the rows in order to find which ones contain "229.62.232.190"
for row in rows:

    # If "229.62.232.190" is found in a row, then print "COMPANY SERVER FOUND" and user info
    if(row.find("229.62.232.190") > -1):
       
        print("COMPANY SERVER FOUND")
        # Split the current row on commas
        info = row.split(",")
        # Print out the user's name, password, and hours online
 

        # Split the IP column into a list on semicolons
  

        # Loop through the ip_list and print them to the screen
        print("IPs:")