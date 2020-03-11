# Import the secrets, os, and zipfile modules
import secrets
import os
import zipfile

# Create an empty list that will be used to store all of the words later on
completeWordList = []

# Create a connection to the "WordList.zip" file
zippedFile = zipfile.ZipFile("WordList.zip")

# Exctract all of the files inside of "WordList.zip"
zippedFile.extractall()

# Create a path to the newly created "WordList" folder
wordListFolder = os.path.join("WordList")

# Use os.walk() to navigate through the text files within the "WordList" folder
for root,dirs,files in os.walk(wordListFolder):

    # Loop through the files at the current root
    for oneFile in files:

        # Create the path that points to the current file
        filePath = os.path.join(root, oneFile)

        # Create a connection to this file in read mode and read its contents
        openPath = open(filePath)
        wordsText = openPath.read()
     

        # Split the wordsText variable on newlines
        splitWordsText = wordsText.split("\n")


        # Loop through each element in the splitWordsText list
        for word in splitWordsText:

            # Push the word into the completeWordList
            completeWordList.append(word)

# Variable to store the passphrase
passphrase = ""

# Loop for however long you want the passphrase to 
#using for over while because while requires more code. need a way to break a while loop without user interaction
for i in range (4):

  # Select a random word using the secrets module and add it to the passphrase
  passphrase += secrets.choice(completeWordList).capitalize()
  
# Print out the passphrase
print(passphrase)