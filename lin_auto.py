import os

while 1:
    print("""
    Option 00: Exit.
    Option 01: See all the runing processes.
    Option 02: Clear Screen.
    Option 03: Check IP address.
    Option 04: Check current date.
    Option 05: Check Time.
    Option 06: Open Calendar.
    Option 07: Put program to sleep for n seconds.
    Option 08: List files in current directory.
    """)

    choice = input()

    if choice == 0:
        exit()
    elif choice == 1:
        os.system("top")
        os.system("read -p \"press enter to continue\"")
    elif choice == 2:
        os.system("clear")
    elif choice == 3:
        os.system("ifconfig -a")
        os.system("read -p \"press enter to continue\"")
    elif choice == 4:
        os.system("date")
    elif choice == 5:
        os.system("date +%T")
    elif choice == 6:
        os.system("cal")
        os.system("read -p \"press enter to continue\"")
    elif choice == 7:
        print("For How Long")
        time = int(input())
        os.system("sleep " + time)
    elif choice == 8:
        os.system("ls")
        os.system("read -p \"press enter to continue...\"")
    else:
        print("Please Choose a valid option!")