import os
import shutil
def pptx_copy():
    #create variables to specify the path to the source and destination of the file
    source = (r"c:\Users\jclem\Downloads")
    dest = (r"c:\Users\jclem\Documents\Python")
    # get to each file in the directory
    for files in os.listdir(source):
        # make a connection between the source of the file and the individual file that wil be pulled
        Path = os.path.join(source, files)
        # create an if statement to grab the files based on the extension
        # In this case we use .endswith() to pull .pptx or .ppt files
        if files.endswith(".pptx") or files.endswith (".ppt"):
            # finally, we use the shutil module to copy and move the file
            # we specify the Path variable instead of source because we specified the source connection there and the dest variable for where it ends up
            shutil.copy(Path, dest)





pptx_copy()            
    
    
    
    