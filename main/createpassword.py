from variables import *

def CreateAPassword():
    from tqdm import tqdm
    import string
    import random

    #Local Variables
    Password = ""               #Is the password before removal of RestrictedCharacters
    SecurityType = 0            #Indicates if user choice is basic, medium or hard
    IsSecurityTypeDone = 0      #Indicates if SecurityType selection loop is done
    PasswordLength = 0          #Indicates Password Length
    IsLengthDone = 0            #Indicates if PasswordLength is set a value
    IsRestrictionDone = 0       #Indicates if RestrictedCharacters
    RestrictedCharacters = []   #Indicates which characters will be removed in the final password
    RestrictedCharactersText = ""   #Used to convert Restricted to text
    temp_Password = ""          #Converts Password to list
    final_Password = ""         #Is the final password
    CharacterToBeAppended = ""  #Holds which character will be added to RestrictedCharacters

    print("   ___              _                ___                              _ ")
    print("  / __|_ _ ___ __ _| |_ ___   __ _  | _ \__ _ _______ __ _____ _ _ __| |")
    print(" | (__| '_/ -_) _` |  _/ -_) / _` | |  _/ _` (_-<_-< V  V / _ \ '_/ _` |")
    print("  \___|_| \___\__,_|\__\___| \__,_| |_| \__,_/__/__/\_/\_/\___/_| \__,_|")
    print("'----------------------------------------------------------------------------'")
    #Length choice
    while IsLengthDone == 0:
        PasswordLength = int(input("How long do you want your password to be? \nNOTE: Maximum input is 100 \nType a number: "))
        if PasswordLength > 0 and PasswordLength <= 100:
            IsLengthDone += 1
        else:
            print("Invalid Length!")

    #Removal of characters
    while IsRestrictionDone == 0:
        CharacterToBeAppended = str(input("Would you like to restrict any characters? \nType an input, leave blank to cancel "))
        if CharacterToBeAppended != "":
            RestrictedCharacters.append(CharacterToBeAppended)
        elif CharacterToBeAppended == "":
            IsRestrictionDone += 1

    #Generates password
    while IsSecurityTypeDone == 0:
        PasswordSecurity()
        SecurityType = int(input("Choose your Security type: "))
        if SecurityType == 1:
            skipline()
            print("You have chosen a Basic security password, which includes Alphabetic values.")
            Password = ("".join(random.choice(string.ascii_letters)for i in range (PasswordLength)))   
            IsSecurityTypeDone += 1
        elif SecurityType == 2:
            skipline()
            print("You have chosen a Medium security password, which include Alphanumeric values.")
            Password = ("".join(random.choice(string.ascii_letters)for i in range (PasswordLength)))
            Password += ("".join(random.choice(string.digits)for i in range (PasswordLength)))  
            IsSecurityTypeDone += 1
        elif SecurityType == 3:
            skipline()
            print("You have chosen a High security password, which include Alphanumeric values and special characters.")
            Password = ("".join(random.choice(string.ascii_letters)for i in range (PasswordLength)))
            Password += ("".join(random.choice(string.digits)for i in range (PasswordLength)))
            Password += ("".join(random.choice(string.punctuation)for i in range (PasswordLength)))
            IsSecurityTypeDone += 1
        else:
            skipline()
            print("Invalid Input.")

    #Scrambles final Password
    RestrictedCharactersText = "".join(RestrictedCharactersText)
    #Password.replace(RestrictedCharactersText,random.choice(string.ascii_letters))
    temp_Password.replace(RestrictedCharactersText,"-")
    temp_Password = list(Password)
    random.shuffle(temp_Password)
    final_Password = "".join(temp_Password)

    #Password loading
    for i in tqdm (range(int(10e6)), desc="Generating Password"):
        pass

    #Password trimming
    final_Password = final_Password[0:PasswordLength] 

    #