import os

print("""
        option 1 - Clear the screen
        option 2 - Exit
     """)

choice = int(input())

if choice == 1:
    os.system("clear")
else:
    os.system("exit")
    