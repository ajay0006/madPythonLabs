#Peter Voisey
#Lab5 - Menu

#Import Statements
import sys #imports sys

#Menu Function
def menu():
    choice=0
    while (choice==0):
        print('''
Hello, Please Select a function to execute:
1 - Vertical Line
2 - Horizontal Line
3 - Staircase
4 - Random Pixel
5 - Backlight
6 - Exit
''')
        choice = input() # Gets users input

        if choice == 1:
            print("1")

        if choice == 2:
            print("2")

        if choice == 3:
            print("3")

        if choice == 4:
            print("Hello")

        if choice == 5:
            print("5")

        if choice == 6:
            print("6")
            sys.exit(0)

menu()

