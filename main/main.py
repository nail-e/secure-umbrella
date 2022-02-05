from unittest import skip
from variables import *         #Imports all variables from variables.py
import time
from tqdm import tqdm           #Imports tqdm, a loading bar
from createpassword import *    #Imports all variables from createpassword.py
from createfile import *        #Imports all variables from createfile.py

#Local Variables 
IsMenuDone = 0 
MainMenuInput = 0

SecureUmbrella_title()
skipline()
for i in tqdm (range(int(5e6)), desc="Initializing"):       #tqdm loading bar that lasts a second (5 million ticks)
    pass
while IsMenuDone == 0:
    mainmenu()
    skipline()
    MainMenuInput = int(input("Choose an option: ")) 
    if MainMenuInput == 1:
        #function for Creating Password
        IsMenuDone += 1
    elif MainMenuInput == 2:
        #function for Store Existing Password
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

