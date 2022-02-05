from variables import *
import time 

if os.path.exists("Saved Passwords"):
    print("Saved Passwords already exists, Continuing...")
    pass
else:
    for i in tqdm (range(int(5e6)), desc="Creating folder 'Saved Passwords'"):
        pass
    NewDirectory()                              #Creates Directory
    print("Folder 'Saved Passwords' created")