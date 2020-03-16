print('''

   __---~~~~--__                      __--~~~~---__
 `\---~~~~~~~~\\                    //~~~~~~~~---/'  
   \/~~~~~~~~~\||                  ||/~~~~~~~~~\/ 
               `\\                //'
                 `\\            //'
                   ||          ||      
         ______--~~~~~~~~~~~~~~~~~~--______              
    ___ // _-~                        ~-_ \\ ___  
   `\__)\/~                              ~\/(__/'          
    _--`-___                            ___-'--_        
  /~     `\ ~~~~~~~~------------~~~~~~~~ /'     ~\        
 /|        `\         ________         /'        |\     
| `\   ______`\_      \------/      _/'______   /' |          
|   `\_~-_____\ ~-________________-~ /_____-~_/'   |  
`.     ~-__________________________________-~     .'       
 `.      [_______/------|~~|------\_______]      .'
  `\--___((____)(________\/________)(____))___--/'     

               Welcome to Lambo Nights! 
                   Let's drive....

                © Lambo Nights 2020   

   ''')

print("""
You will now have to text your way around your garage and find a way
to drive to the race track! Hurry! Time is not on your side! 
""")

print("""
You are now in front of your car within your garage. 
Note: You must follow all safety and laws!

Tips: Type Help for user actions.
start - to turn on your car
stop - to turn off your car
quit - to quit
Buckle - Put your seat belt on
Mirrors - Check all mirrors
Clicker -Open garage
D - put car in Drive
P - Put car in Park
R - put car in Reverse
map - View the entire map
unlock - Unlock your car
lock - Lock your car


""")
command = ""
start = False
stop = False
buckle = False
mirrors = False
clicker = False
drive = False
park = False
reverse = False
unlock = False
lock = False

help = """
start - to turn on your car
stop - to turn off your car
quit - to quit
buckle - Put your seat belt on
mirrors - Check all mirrors
clicker -Open garage
drive - put car in Drive
park - Put car in Park
reverse - put car in Reverse
map - View the entire map
unlock - Unlock your car
lock - Lock your car
"""

while True:
    command = input("You are in front of the driver door. What would you like to do?: ").lower()
    if command == "unlock":
        if unlock:
            print("Car is already unlocked")
        else:
            unlock = True
            print("Beep Beep...Your car is now unlocked")
            break
    elif command == "quit":
        break
    else:
        print("Sorry, that's not possible.")


while True:
    command = input("Okay, it's time to start! You are in your car. What would you like to do?: ").lower()
    if command == "buckle":
        if buckle:
            print("You are already buckled up!")
        else:
            buckle = True
            print("You have buckled up!")
            break
    elif command == "quit":
        break
    else:
        print("Sorry, that's not possible.")


while True:
    command = input("Okay, you have buckled up. What else should you check prior to starting your car?: ").lower()
    if command == "mirrors":
        if mirrors:
            print("You have already checked your mirrors")
        else:
            mirrors = True
            print("Perfect! You can now safely see from all sides.")
            break
    elif command == "quit":
        break
    else:
        print("Sorry, that's not possible.")


while True:
    command = input("All safety checks are completed. Your car is not on. What would you like to do?: ").lower()
    if command == "start":
        if start:
            print("Your car is already on.")
        else:
            start = True
            print("Engine starts up! Nicely done. ")
            break
    elif command == "quit":
        break
    else:
        print("Sorry, that's not possible.")


while True:
    command = input("Engine is now on and you are ready to go! What would you like to do now?: ").lower()
    if command == "drive":
        if drive:
            print("Your car is already in Drive")
        else:
            drive = True
            print("Great! Your car is now in Drive and you are now driving out!: ")
            break
    elif command == "quit":
        break
    else:
        print("Sorry, that's not possible.")


