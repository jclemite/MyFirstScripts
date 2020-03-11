# Create a function that will ask what the user wants to do, and returns the user's choice back to the main program/file. 
def userChoice():
    choice = input("Would you like to read the file, write to the file, or quit the file? ")
    if (choice == "read"):
        return "Read"
    elif(choice == "write"): 
        writeFile = open("WatchList.csv", "w")
        writeFiles = writeFile.write()
        print("What would you like to write? ")

    elif(choice == "quit"):
        print("Go in peace")

    else:
        print("Can you read lmao")


# Create a function that will read the external file and print out the data it contains. Remember to split the text as this is a CSV file.Close the connection to your external file at the end.
def readFile():
    fileName = open("WatchList.csv", "r")
    fileNames = fileName.read()

    fileRows = fileNames.split("\n")
    print(fileRows)
    fileCells = fileRows.split(",")
    print(fileCells[0])
    print(fileCells[1])
    print(fileCells[2])
    print(fileCells[3])


# Create a function that will write a new row of data into the external file, but will not overwrite what is already there. This will require you to also collect that input from the user. When writing to your file, rememer to add in the necessary commas and line break. 
def writeFile()

# Collect the user's initial choice


# Run a while loop that includes how the program will as long as the user selects either the Read or Write choice. so long as the user's choice is "1" or "2"


# Print out "THANK YOU FOR USING THE WATCHLIST"