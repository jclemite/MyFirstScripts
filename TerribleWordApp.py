# Set the variable continueWriting to "y" to start things off
continueWriting = "y"
# Establish a connection to "Notes.txt" and set the mode to "write"
variable = open("notes.txt", "w")

# Check if the user would like to write some more text to the page
while(continueWriting == "y"):

    print("\n---------------\n")
#askUser = input("Would you like to write more on the next page? ") 



    # Ask the user to enter some text and save it to a variable
    toWrite = input("Please enter some text to write.. \n")
  
    # Use notesFile.write() to push the text in the above variable to the external file
    
    variable.write(toWrite)


    # Add a newline character after the entered text
    variable.write("\n")
    print("\n-----------------\n")
    # Ask the user if they would like to write another line
    
