from variables import *
import string
import random

#Local Variables
Password = ""               #Is the final password
SecurityType = 0            #Indicates if user choice is basic, medium or hard
IsSecurityTypeDone = 0      #Indicates if SecurityType selection loop is done
Syntax_a = ""               #Syntax Seed for Uppercase
Syntax_b = ""               #Syntax Seed for Lowercase
Syntax_c = ""               #Syntax Seed for Numbers
Syntax_d = ""               #Syntax Seed for Punctuation
PasswordLength = 0          #Indicates Password Length
IsLengthDone = 0        #Indicates if PasswordLength is set a value

#ADD DEF FOR CREATE PASSWORD
print("   ___              _                ___                              _ ")
print("  / __|_ _ ___ __ _| |_ ___   __ _  | _ \__ _ _______ __ _____ _ _ __| |")
print(" | (__| '_/ -_) _` |  _/ -_) / _` | |  _/ _` (_-<_-< V  V / _ \ '_/ _` |")
print("  \___|_| \___\__,_|\__\___| \__,_| |_| \__,_/__/__/\_/\_/\___/_| \__,_|")
print("'----------------------------------------------------------------------------'")
while IsSecurityTypeDone == 0:
    PasswordSecurity()
    SecurityType = int(input("Choose your Security type: "))
    if SecurityType == 1:
        print("You have chosen a Basic security password, which includes Alphabetic values.")
        Syntax_a = ("".join(random.choice(string.ascii_uppercase)for i in range (10)))
        Syntax_b = ("".join(random.choice(string.ascii_lowercase)for i in range (10)))      
        IsSecurityTypeDone = IsSecurityTypeDone + 1
    elif SecurityType == 2:
        print("You have chosen a Medium security password, which include Alphanumeric values.")
        Syntax_a = ("".join(random.choice(string.ascii_uppercase)for i in range (10)))
        Syntax_b = ("".join(random.choice(string.ascii_lowercase)for i in range (10)))
        Syntax_c = ("".join(random.choice(string.digits)for i in range (10)))  
        IsSecurityTypeDone = IsSecurityTypeDone + 1
    elif SecurityType == 3:
        print("You have chosen a Medium security password, which include Alphanumeric values and special characters.")
        Syntax_a = ("".join(random.choice(string.ascii_uppercase)for i in range (10)))
        Syntax_b = ("".join(random.choice(string.ascii_lowercase)for i in range (10)))
        Syntax_c = ("".join(random.choice(string.digits)for i in range (10)))
        Syntax_d = ("".join(random.choice(string.punctuation)for i in range (10)))
        IsSecurityTypeDone = IsSecurityTypeDone + 1 
    else:
        skipline()
        print("Invalid Input.")

while IsLengthDone == 0:
    PasswordLength = int(input("How long do you want your password to be? "))
    
