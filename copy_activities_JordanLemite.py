import os
import shutil

def stu_activities():
    # create a variable that = what we are looking for
    strName = "README"
    # establish the location of the directory we are searching and where we are copying to
    source = (r"c:\Users\jclem\Downloads")
    dest = (r"c:\Users\jclem\Documents\Python")
    # create a for loop to get to each file in the directory
    for i in os.listdir(source):
        #make a connection between the source of the file and the individual file that wil be pulled
        Path = os.path.join(source, i)
        # use contains to search i which now contains the source for the string name 
        # print to show what to look for aka what was found 
        if i.__contains__(strName):
            print(i)
            shutil.copy(Path, dest)




stu_activities()