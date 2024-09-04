# PASSWORD  GENERATOR

import random
import string

def generate_password(length):
    # Define the characters to use for the password
    characters  = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password 

def main():
    #prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password:"))
    
    #Generate the password
    password = generate_password(length)
    
    # Print the generated password
    print("Generated Password:", password)
    
if __name__ == "__main__":
    main()