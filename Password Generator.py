import string
import random

if __name__ == '__main__':

    lowerCase = string.ascii_lowercase
    upperCase = string.ascii_uppercase
    digits = string.digits
    specialChar = string.punctuation

    #user inputs for social handles and password length
    socialHandle = input("Enter the social handle you want to create the password for: ")
    try:
        passLen = int(input("Enter the password length: "))
    except ValueError:
        print("Expecting an integer input!")

    #creating list for the possible characters for the password
    charList = []
    charList.extend(lowerCase)
    charList.extend(upperCase)
    charList.extend(digits)
    charList.extend(specialChar)
    random.shuffle(charList)
    
    #generating final password
    genPass = "".join(charList[0:passLen])

    with open("passwords.txt", "a") as passfile:
        passfile.write(socialHandle)
        passfile.write("  -  ")
        passfile.write(genPass)
        passfile.write("\n")





     
        

