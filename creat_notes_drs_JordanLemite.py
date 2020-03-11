#define a function called main
#import the os module for use in creating directories
import os

def main():
    #create a directory called Cyber Security-Notes
    # make an if statement to check for the directory and create it if not found 
    if not os.path.exists('CyberSecurity-Notes'):
        os.mkdir('CyberSecurity-Notes')
# create the path the folder just created
    #os.mkdir(r'c:\Users\jclem\Documents\Python\CyberSecurity-Notes')    
    rootpath = r'c:\Users\jclem\Documents\Python\CyberSecurity-Notes'
    # create the for loop to loop through 24 times
    for x in range(1,25):
        # change directory to the folder created
        os.chdir(rootpath)
        # specify the string that will be created 24 times and create the directory 
        dirName = "week" +str(x)
        os.makedirs(dirName)
        # we need this to specify that the next variable string will be inside the folders just created
        # if not done, then the next loop will loop along side instead of being in the correct spot
        pathTwo = rootpath+ '/' + dirName
        os.chdir(pathTwo)
        # this for loop only needs to loop through 3 times for each folder
        for i in range(1,4):
            # specify the string that will be created 
            subdir = "Day" +str(i)
            os.makedirs(subdir)
    

main()