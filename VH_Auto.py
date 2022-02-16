import os
import os.path
from os import path

while 1:
    print("\n                                   ========== Choose from the following options ==========")
    print("""
             option 00: Exit.
             option 01: Run any CMD command.
             option 02: Task Manager.
             option 03: Clear Screen.
             option 04: Check IP address.
             option 05: Check current Date.
             option 06: Check current Time.
             option 07: Open Windows Calendar.
             option 08: Get help for a command.
             option 09: Create a timer.
             option 10: Open firefox installed in your pc.
             option 11: print some text on screen.

             ========================================================================================

             Please Enter your choice...
        """)
    #solves a bug where giving invalid values causes an error 
    ch = input()
    if (ch.isdigit()):
        choice = int(ch)
    
    #Choices Code
    if (choice == 0):
        os.system("Exit")
        break
    elif (choice == 1):
        print("Type the command you wish to run")
        cm = str(input())
        os.system(cm)
    elif (choice == 2):
        os.system("taskmgr")
    elif (choice == 3):
        os.system("cls")
    elif (choice == 4):
        os.system("ipconfig")
        print("\nPress Enter to continue...")
        input()
    elif (choice == 5):
        os.system("date")
    elif (choice == 6):
        os.system("time")
    elif(choice == 7):
        os.system("start outlookcal:")
    elif (choice == 8):
        print("Type the command you want get help of...")
        cm = str(input())
        os.system("HELP " + cm)
        print("Press Enter to continue...")
        input()
    elif (choice == 9):
        print("How long(in seconds)")
        t = int(input())
        os.system("timeout " + str(t))
    elif (choice == 10):
        os.system("start firefox")
    elif (choice == 11):
        print("Enter the text you want to print")
        text = str(input())
        print(text)
        print("\nPress Enter to continue...")
        input()
    else :
        print("No such Option exist please choose a valid option")
        print("Press Enter to conitnue...")
        input()