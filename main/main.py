from unittest import skip
from variables import *         #Imports all variables from variables.py
import time
from tqdm import tqdm           #Imports tqdm, a loading bar
from createpassword import *    #Imports all variables from createpassword.py


SecureUmbrella_title()
skipline()
for i in tqdm (range(int(5e6)), desc="Initializing"):       #tqdm loading bar that lasts a second (5 million ticks)
    pass
HomeMenu()
