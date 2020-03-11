# Import the two modules that will be used in this code

import os
import datetime

#create connection to csv file

csvFile = open("RedFlags.csv", "w")

# Since there are so many files, os.walk would be wise
for root, dirs, files in os.walk('Text'):

    print("GETTING FILE INFO")
    
    # Loop through all of the files in the current root
    for oneFile in files:

        # Create the path to the current file
        filePath = os.path.join('Text')

        # Get the stats on the file, save to fileInfo variable
        statInfo = os.stat(filePath)

        # Collect the last time at which the file was modified
        timeModified =  statInfo.st_mtime

        # Change the format of timeModified to datetime format
        from datetime import datetime
        datetime.fromtimestamp(timeModified).strftime('%c')

        # Collect the file size of the file
        statInfo.st_size

        #write the new line of data into the external csvfile

        csvFile.write(filePath, statInfo.st_size,timeModified, "\n")

        # Print out the file name timestamp, and size to the screen
        #in order to use plus symbols instead of commas, you'd have to convert statInfo.st_size to a string
        #print("File Name: ", oneFile, "Timestamp: ", timeModified, "Size of the file: ", statInfo.st_size)

        csvFile.close()

