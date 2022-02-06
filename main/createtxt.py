def CreateTxt():
    import os
    import time 
    from createpassword import final_Password
    from tqdm import tqdm
    from variables import NewDirectory
    from variables import PasswordChoice

    #Local Variables
    SiteName = ""
    LoginName = ""
    ExistingPassword = ""
    FileName = ""

    if os.path.exists("Saved Passwords"):
        print("Saved Passwords already exists, Continuing...")
        pass
    else:
        for i in tqdm (range(int(5e6)), desc="Creating folder 'Saved Passwords'"):
            pass
        NewDirectory()                              #Creates Directory
        print("Folder 'Saved Passwords' created")

    SiteName = str(input("Which site is this login used for? "))
    FileName = SiteName + ".txt"
    LoginName = str(input("What is the login for the site? "))
    LoginName = "Login: " + LoginName
    final_Password = "Password: " + final_Password

    if PasswordChoice == "y":
        #Find way to save in Saved Passwords
        with open(FileName, "a") as f: 
            print(SiteName, file=f)
            print(LoginName, file=f)
            print(final_Password, file=f)
    elif PasswordChoice == "n":
        ExistingPassword = str(input("What is your password for the site? "))
        ExistingPassword = "Password: " + ExistingPassword
        with open(FileName, "a") as f:
            print(SiteName, file=f)
            print(LoginName, file=f)
            print(ExistingPassword, file=f)