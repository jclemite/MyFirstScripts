# Import the zipfile module into the application
import zipfile

# Create another reference, this time to a locked ZIP file
zipLocked = zipfile.ZipFile("MusicSheets.zip")


# Variable used to store the password string
password = "ComicSans"

# Run the `.extractall()` function with a password

zipLocked.extractall(pwd=password.encode())