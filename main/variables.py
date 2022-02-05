#Variables.py

#Dictionary
import os
from tqdm import tqdm

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
    print("")
    print("Save New Password?")
    print("[y/n]")

#Part of createfile.py

def NewDirectory():
    if not os.mkdir("Saved Passwords"):
        os.mkdir("Saved Passwords")
        for i in tqdm (range(int(5e6)), desc="Creating folder 'Saved Passwords'"):
            pass
        print("Created folder for Saved Passwords")
    else:
        print("Folder already Created")

#def NewFile():