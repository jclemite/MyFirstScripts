# Create a function which takes in a word and then searches for the word within the text
def wordSearch(word): 

    # Open up the file called "Monologue.txt"
    monologueFile = open("Monologue.txt")
    # Read the text contained within the file
    monologueText = monologueFile.read()

    # Add a space before the word so as to make sure that it is independent
    space = (" " + word + " ")

    # Search for any instances of the word provided
    if (monologueText.find(space) > -1):


        # If the word is found, count up how many times it appears by splitting the text on the word and counting the length of the list returned
        countList = monologueText.split(space)
     

        # Print out how many times the word was found
       
        print ("The word" + space + " can be found " + str(len(countList) -1) + "times")
    # If no instances of the word was found, print out that the word is not in the text
    else:
        print("The word" + space + " is not in the text")

# Collect a word from the user

wordToSearch = input("Please enter a word to search for: ")

# Pass the word to search into the function created
wordSearch(wordToSearch)