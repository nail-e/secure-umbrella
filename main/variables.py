#Variables.py

#Dictionary
from locale import currency
import os
from tqdm import tqdm

#Part of main.py

def HomeMenu():
    #Local Variables 
    IsMenuDone = 0 
    MainMenuInput = 0
    from createpassword import CreateAPassword
    from createtxt import CreateTxt

    while IsMenuDone == 0:
        mainmenu()
        skipline()
        MainMenuInput = int(input("Choose an option: ")) 
        if MainMenuInput == 1:
            CreateAPassword()
            IsMenuDone += 1
        elif MainMenuInput == 2:
            CreateTxt()
            IsMenuDone += 1
        elif MainMenuInput == 3:
            #function for S
            IsMenuDone += 1
        elif MainMenuInput == 4:
            print("Exiting Program")
            IsMenuDone += 1
        else:
            skipline()
            print("Invalid Input!")


#Title that prints Secure Umbrella title
def SecureUmbrella_title():
    print(" ____                             _   _           _              _ _       ")   
    print('/ ___|  ___  ___ _   _ _ __ ___  | | | |_ __ ___ | |__  _ __ ___| | | __ _ ')
    print("\___ \ / _ \/ __| | | | '__/ _ \ | | | | '_ ` _ \| '_ \| '__/ _ \ | |/ _` |")
    print(" ___) |  __/ (__| |_| | | |  __/ | |_| | | | | | | |_) | | |  __/ | | (_| |")
    print("|____/ \___|\___|\__,_|_|  \___|  \___/|_| |_| |_|_.__/|_|  \___|_|_|\__,_|")

def mainmenu():
    print(" __  __")              
    print("|  \/  |___ _ _ _  _ ")
    print("| |\/| / -_) ' \ || |")
    print("|_|  |_\___|_||_\_,_|")
    print("'----------------------'")
    print("[1.] Create Password")
    print("[2.] Store Existing Password")
    print("[3.] View Stored Passwords")
    print("[4.] Exit")
                      
def skipline():
 print("")

#Part of createpassword.py

def PasswordSecurity():
    print("")
    print("Security Types")
    print("[1.] Basic (A-Z & a-z Only)")
    print("[2.] Medium (A-Z, a-z & 0-9)")
    print("[3.] High (A-Z, a-z, 0-9 & Special Characters)")

def SaveNewPassword():
    from createpassword import final_Password
    from createtxt import CreateTxt
    global PasswordChoice

    PasswordChoice = ""
    print("")
    print("Save New Password?")
    PasswordChoice = str(input(("[y/n] ")))
    if PasswordChoice == "y":
        #Insert function for create.txt
        CreateTxt()
        pass
    elif PasswordChoice == "n":
        print("Your to-be password was", final_Password)
        HomeMenu()

#Part of createtxt.py
CurrentFolder = os.getcwd

def NewDirectory():
    os.mkdir("Saved Passwords")

#def NewFile():
