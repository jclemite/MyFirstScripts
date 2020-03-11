# Create an application that will ask the user for the name of a text file.
import os
askUser = input("Which file are you looking for? ")
# Then checks to see if the file exists in the Books folder.
real_path = os.path.join("Books", "Dracula.txt", "Frankenstein.txt", "PrideAndPrejudice.txt")
# If the text file exists, then print the text inside of the file to the terminal.
#DracFrankPAP = open(real_path)
filePath = os.path.join("Books", askUser + ".txt")
if os.path.isfile(filePath):

    #create a connection to the file
    bookFile = open(filePath)

    #read in the text that the file contains
    bookText = bookFile.read()

    #Print contents to terminal

    print(bookText)
# If the text file does not exist, then print "Sorry! That book is not in our records! Please try again!"
else :
    print("Sorry! That book is not in our records! Please try again!")
# Hint: When the user enters the file name, keep in mind that they will not use a file extension (.txt).
# Therefore, when you’re creating your file path, remember that you’ll need to have the file extension added to that user input.
