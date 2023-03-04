#IMPORTS
import sys
import time
import random, string

#CODE

unlocked = False
print("Welcome to this basic python text-based computer system. You can use it to do many basic tasks. ")
username = input("Please input your username for identification purposes ")
if username == "n":
    print("You have succesfully been identified!")
    password = input("Now, please enter your password for security purposes. If you can't remember your password, type 'Forgot'. Please note, for security, it is case-sensistive. ")
    if password == "1234":
        unlocked = True
        print("You have successfully logged in. Please wait while the system loads up!")
    if password == "Forgot":
        print("You have forgotten your password. To prove you are a human, type out the following letter. It is case-sensitive.")
        randomLetter = random.choice(string.ascii_letters)
        antirobot = input(randomLetter)
        if antirobot == randomLetter:
            print("You have succesfully verified you are not a robot. Please contact a system administrator to continue.")
            time.sleep(2)
            
        else:
            print("Suspicious behaviour detected. Aborting...")
            sys.exit()
    if password != "1234":
        print("   ")
        print("You have either inputted an incorrect password or are waiting for assistance from a sytem administrator.")
        print("Please wait...")
        time.sleep(2)
        password2 = input("Please enter your password. Please note, you have no attempts remaining if this is incorrect")
        if password2 == "1234":
            print("You have successfully logged in. Please wait while the system loads up!")
            time.sleep(3)
        else:
            print("Suspicious behaviour detected. Aborting...")
            sys.exit()
else:
    print("Your username couldnt be identified. Please contact a system administrator if this isssue persists")
    print("Due to technical limitations, the program will automatically stop in abut 15 seconds and must now be restarted manually.")
    time.sleep(15)
    sys.exit()


print("Your basic python computer is now ready to use")
