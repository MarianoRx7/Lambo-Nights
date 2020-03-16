import sqlite3

conn = sqlite3.connect('cargame.db"=') # get a connect object
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS counts''')

cur.execute('''
CREATE TABLE Level (progress NUMERIC)
CREATE TABLE Users (name TEXT email BLOB password BLOB)''')


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
buckle - Put your seat belt on
mirrors - Check all mirrors
clicker -Open garage
drive - put car in Drive
park - Put car in Park
reverse - put car in Reverse
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
    command = input("Engine is now on and you are ready to go! Note: Your garage is still closed. What would you like to do now?: ").lower()
    if command == "clicker":
        if clicker:
            print("Your garage is already open.")
        else:
            clicker = True
            print("As your garage door opens, you rev the engine with anticipation: ")
            break
    elif command == "quit":
        break
    else:
        print("Sorry, that's not possible.")

while True:
    command = input("Garage is finaly open! What would you like to do now?: ").lower()
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

print('''
     
clllccccc:cccccccccccclllcccccccccc::::cccccccccccc:ccccllcc:;;;cccccccc::cc::;::::cc::::cllcc:::ccll:;;::cclllcccccc::;;::::::lodddodddddddddddddddddddooooooooooodollooolllllllllllllllllllllllllclllllllllllloooooooloooooooooolllllllllllllccccllllclllllllllllllllllllllllcllcccccllllcclllllllllllllllllllllccccccccccclccccccccccccccccclcc:;;:::::::;;
::cc:::::::::::::::ccccccccccccccccccccccccccccccccccccccc:::;;:ccccccccccc::::ccccccccc:cccc:::::ccc:::cccccccccc::::c:::::::;::cc:cccclcccccllclllllllllllllloooodolllllllllcccllllllccccccccclllllllllccccccllllcclllllllllccccccccccccllcllcccccclcccccccccccccccccccclc:::cc::::::ccc:ccc::ccccc::c::::::::::::::,'';;,;::;,'';::;:cccc:;;;;;;;;,,,
;;;;;;;;;;;;;;;;;;;;;;;;;;::;::;::::::;::::::::::::::::::::::::::::::::c::::::::::::::::::::;::::::;:::;:::::::::::::::::::::::::c:::c:::ccccccccclllllcclllllllcclllooooollcc:::clllloolccccllllooolllllllllllolllllcccccccccccccccccccccccccc:cccccccccccccccccccccccllccclccccc::::cccc::cc:c:::ccccccclc:cccclccc:;,,;:;;;;::;;:::;;;:ccccllcccclc::::;;,,
;;;;;;;;;;;;;;;;;;;;::::;:::;::::::::::::::::::::::::::::::::::::::::::c::::::;;::::::::::::::::::::cc::c:;:::;:::::;:c::ccc::cc::::::::lcccccccclllllllllcclllcccllllllcc::::;::;;;;;;::::::::::llll;;;;;;;;;;;;;;;;;;::ccccccccllllcccclc:;;cc:cccccccccccc::cccccccc::cccccclccccclc:lolllcc:clc:clllc:clllcccc::::c:::
;;;;;;;;;::;;;;;;;;;;;::::;;;;;;;;::;;;;;;;;;;;;;;;;;;::;;:::::::::;:::;:c:::::;;;;;;;::::::::::::::c:::::::::::ccccccllllllllolcloolc:clclodolloolccccllcccclllcccc::;;:;;;;::::::::::::::::::::llll;;;;;;;;;;;;;;;;;;;;;lodddddddddddddoodllooloollcllc::coooollllllllllcllcloocclolollllooooc:lc:llllllllccccc:clllcclllllllcclcllc::cccccc:cllll::cl::cc::c
;;;;;;;;:;;;;:;;;::;;;;;::;::;;;;;::;;;;:;;;;;;;::;::;,;;:::;;::::::;::;:c:::;;:;;;;::;;;::cccc::::ccclc:ccclccloooddxxxxdoodxxdddddll::cccllllloollllccccccccc:;;;;;;;;;;;;;::::::::::::::::::::lll:::::::::::::::::::::::oooooooooddddddddddddddoooooddooddool,'clc:;,clcc:;llllccodlcclloddllc:;clolloollooc:::;cllllcloooollollol::clcll:;;;:ll:::cc:ccccc
;;;;;;;;;;;;;;;;;;::;,;cc:::::;;::;;;;:::::::;;;;;;::;;:::::;;:;,;;;;:::::;;::::::::llcccccooool:loolldolllloolldddxddxkkxxxxddoooolccclllllllcccccccccccc:;,,,;;;;;;;;;;;;;:::::::;:::::::::::::llll:::::::::::::::::::::::::::cccloooooooooooddddddddddddodoool;,;llc;;:,,:loolcclllccllcclolclooc,,:oolc::lddlclllodxol:;clclooclllolllcooc,',:c:::cccc:;;;;
;,,:c:::;;::::;;;::;,.,clccccc;,;;,';:c:::cl::;:c:;;;::ccccccllooolllllloooooodxddxxxdxxkxdllxdloddxxxxxdxxkxxxxddxdoooollllllccllollccc:::cllcc:;,,,,,;;;,,,,,,,,,,;,,,;;;;;;;;;;;;;::::::::::::llll:::::::::::::::::::::::::::cllcccccclllllllllllloollooodooooodooddooooolooddooolod:..,clc::lll::::ll:,;:clol:cclldxoc;:llcloc;;:coooc;clc:::;,:oolllc;;;;;
;;;;;;;::;;:::::;;;;:llcc:;;;,;cc:cccc:'.....'collclloooddddxxxkxxxxxxxxxxxxxkkxxxxxxxooddloxdodxddxxxxxooxdoolccolllllccllccccccc:;;:ccclc:;,,,,,,,;;,,,,,,,,,,,,,;;:::;;;,:::::::;:::::::::::::llll:::::::::::::::::::::::::::;;:::cccclllooooooloooooooddddxdooddddoddddddol::cloolcclooolllll:....,collcccccl:'',:ooccccccclllc;;cccll:;;:c:c;'':l::
c:;;;,;::;;:cc:,.........':looo:::;:cllclooolcccc::ldxxxxxxxxxkkkkkkxxddxkxxolodddxxxddxxxxxddxxxxkkxxxxxxdxxdollllllcclllcccccccccc:;;:cllcc:;,,,,,,,,,,,;;;;;;;;;;;;;:::::::;::::::::::::::::::llll:::::::::::::::::::::::::::c:;;;;;;;:cllloooddddoodddddxdlcodddoddooodoooddooooooloooddol:;,,,,;coooollc;..   lc:lo:.:c:::::;:cllclcccccc:;:cc
l:;;;;;;,,cc:'..........':llddoddooodddxxxxxxxxdooxxdxxxxxxxxxxxxxkkxdoodxkxxdxxollooxxdxxdxkkxxxxxxxxxxddooollccclccccllllcccc:;;:cclccc:;,,,,,,,,,,,;;;;;;;;;;;;;:::::::;::::::::::::::::::::::llll:::::::::::::::::::::::::::c:;;;;;;;:clloddoddoddddxdodxxxdxxddddddddddoddoloddddooooddddooddddddoc;,;:lccll:,;ccc;;;c:;,:loodlcoolc;;cc
;;;:ll:clllc:;ccllccllooddxxxxxxxxxxxxxxxxxkdoodooxxxxxxxxxxkkxddxxdccloolldxdddddxlcldxxdodxdxxddooooolcccclllclllcccccc:;;;;:clllc:;;,,,,,,,,,,,;;;;;;;;;;;;;:::::::;::::::::::::::::::::::::::llll::::::::::::::::::::::::c:;;;;;;;:::::::::cllllloolodxddddxxdddddxddddddddddddddddddddddoloodddoooollloddlc::llloloolllc...;llc:clccllll
clodxxdxxxloddxxdxdoodxd:,lxxxxxxxxdoddxxxxxdodddddddxxxxxdclxl:oddl::llolldxdxxxdloollllolccclccllllccclcclllccc:::;;;;;:ccllcc:;,,,;,,,,,,,,,,,;;;;;;;;;;;;;:::::::;:::::::::::::::::::::::::::llll::::::::::::::::::::::::c:;;;;;;;:::::::::;;;;::::cloooododddddddddddddddddddddddddddolcoddddoooolodxdolccloolooolllc,....',,,;:cccccc:c
dddxxxxxxxdxkxddxxd;,oxdl;cdxxxxxxdoodxxxxxxxxxkkdlldxxxxxl:cddoddxxdxxdoc,,:llcc:;cllllllc::clllllolllllccc:;;;,,,;::clllccc:;,,,,,,,,,,,,,,',,,',,,;;;;;;;;;;;;;,,lkOo;;;;;::ccc::::;;::;;;;;;:llll;::::::::::;;;;;;;;:::::::::::::::;;,;;,,;;;::;:;,;:;;cccllllloooooooddoddodxdddddddddc,:odddddddddooooooolloooollooollllllclol:;;oolllccc
dodxxxxxl::odccodxdl:;cdoc:dkkxxxlcoxxxxxxxxxxxxxdoxxxxddxddddxxxxddl:c:,,;,;:cccccclollllccclllllllc::;;;;;;,,;:clllccccccc,,,,,,,,,,,,,,,;;;;;;;;;;;;,,;::::::;,;;;;::::::::::;;::;;;,;;;;;;;;:llll;:::;;;;;;;;;;::::::::;::::::;;,,,::;;::::ccc:::::::::::cccclccclllooooddodddolodddddoooddolloloooolooolooddoddoooooddooooooooooo
::lddxdolodxxxxxooxkdloddlldxxxxo::oxxxdodxxxxxddoodddxxdddddxxoc::c:;:c;clcllllllc:clcllllllcc:;;;;,,,,,;;:cllllllllllllll:;,,,,,,,,,,,;;;;;;;;;;;;,,,,cooc,,;;;:::::::::::;;;::;;,,;;;;;;;;;;;;llll;;:::;;;;;;,,,;::::::::::::::;,,,,,;:cc:;;;::::c;,:::::::cccclllllooooollooooododdoool,.:oooddolc:cooooooooooooooodddxdoooloo
odddxxxxxxxxxxd:'cxxxxxxxdddxddddddxxddooddxdodxxl::oddoodooolc;;:lllclllc;,:lc::lllllcccc::;;,,;;;;;::llllllllllllllll:;,,,,,,,,;;;;;;;;;;;;,,,;,,,,;;::::::cc::;;;;;;;;;;;;;;;;;;;,,::::::::::,llll;;::;;;;;;;;;;;;;,,,;:::::::::;::;;;;;;;;;;;ccc:,;;,,,,,,,,,,,,,cccccccc:;;:::cclooolcccclllooooooooccodooddooc,;oodlclooloddddddoooolooloo,


''')
