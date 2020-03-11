# Copy and paste your `validate_password` function here
def validate_password(password):
    # Inside the function, check if the password is longer than 6 characters long
    if (len(password) > 6):
        return True
    else:
        return False
    
# Create a function called `collect_user_information` that will prompt the user for their username, password, and email address. It should return this information in a list that contains those three values.

def collect_user_information():
    
    # Prompt the user for their username and store it in a variable called username
    username = input("What's your username? ")

    # Prompt the user for their email and store it in a variable called email
    email = input(str("What is your email address? ")) 
   
    # Prompt the user for their password and store it in a variable called password
    password = input(str("Type your Password here: "))
    
    # Create a list that will store all of the user data collected inside of it and call it user_info
    user_info = [username, email, password]

    # Return the above list (called user_info)
    return user_info

# Create a function called `create_user` that checks if the password entered is valid.
def create_user(user_data):
    username = user_data[0]
    email = user_data[1]
    password = user_data[2]

    # Use your `validate_password` function to check if the password is secure
    if validate_password(password):
        # If yes, create a dictionary, called `user` with the keys "Username", "Email", and "Password" and associate these keys with the values the user entered

        user = {

        "Username" : username,
        "Email" : email,
        "Password" : password
        }    
           
        
        
        # When you're done, use `items` method to print: `"Your username is <USERNAME>"`; `"Your email is <EMAIL"`; and `"Your password is <PASSWORD>"`
        for key, value in user.items():
            print("Your " + key + " is: " + value + ".") 

        # Return user
        return user

    # Otherwise if the password is too short, tell the user to try again
    elif len(password) <=6:
        print("Password is too short")
# Get user information
user_data = collect_user_information()

# Create user
user = create_user(user_data)