import sys
from gfxhat import touch, lcd, backlight, fonts
import time
import random
import signal


# 1. these two functions, displays a vertical line on the gfx hat
# the function below validates a user input, ensuring the gfxhat lcd display constraints are met
def verticalDisplayInput():
    x = int(input("please enter a value less than 128: "))
    if x > 127:
        print("you have entered a number greater than 127")
        x = int(input("please enter a value less than 128: "))
    while x <= 128:
        return x


# this function sets the coordinates for the y axis that prints the vertical line

def verticalDisplay(x=verticalDisplayInput(), y=1):
    while y <= 63:
        lcd.set_pixel(x, y, 1)
        y = y + 1


# 2. these two functions, displays a horizontal line on the gfx hat
# # the function below validates a user input, ensuring the gfxhat lcd display constraints are met
def horizontalDisplayInput():
    y = int(input("please enter a value less than 63: "))
    if y > 63:
        print("you have entered a number greater than 63")
        y = int(input("please enter a value less than 63: "))
    while y <= 63:
        return y


# this function sets the coordinates for the x axis that prints the horizontal line

def horizontalDisplay(y=horizontalDisplayInput(), x=1):
    while x <= 127:
        lcd.set_pixel(x, y, 1)
        x = x + 1


# 3.This program draws staircases on the GFXHat
# clearing the buffer and showing the cleared buffer

lcd.clear()
lcd.show()
# setting values for the variable height and width, this remains constant throughout the program
w = 21
h = 9


# We will be creating eleven functions to depict the lowest building block of each step of the staircase
# the ending point of each x and y points of a function will be the beginning of the next functions' x and y coordinate
# this is to ensure that the lines join properly and to ensure the program is easy to debug

def firstStep():
    for x in range(0, 0 + w):
        lcd.set_pixel(x, 60, 1)


def secondStep():
    for y in range(60, 60 - h, -1):
        lcd.set_pixel(20, y, 1)


def thirdStep():
    for x in range(20, 20 + w):
        lcd.set_pixel(x, 51, 1)


def fourthStep():
    for y in range(50, 50 - h, -1):
        lcd.set_pixel(40, y, 1)


def fifthStep():
    for x in range(40, 40 + w):
        lcd.set_pixel(x, 41, 1)


def sixthStep():
    for y in range(40, 40 - h, -1):
        lcd.set_pixel(60, y, 1)


def seventhStep():
    for x in range(60, 60 + w):
        lcd.set_pixel(x, 31, 1)


def eightStep():
    for y in range(30, 30 - h, -1):
        lcd.set_pixel(80, y, 1)


def ninthStep():
    for x in range(80, 80 + w):
        lcd.set_pixel(x, 21, 1)


def tenthStep():
    for y in range(20, 20 - 9, -1):
        lcd.set_pixel(100, y, 1)


def eleventhStep():
    for x in range(100, 100 + w):
        lcd.set_pixel(x, 11, 1)


# calling a function that calls each function so that the step is drawn

lcd.clear()


def callAllFunctionSteps():
    firstStep()
    secondStep()
    thirdStep()
    fourthStep()
    fifthStep()
    sixthStep()
    seventhStep()
    eightStep()
    ninthStep()
    tenthStep()
    eleventhStep()


# 4 this function adds the duration set by the user in ms to the time real time counter
# this is so that no matter what time the program is run it will clear
def showPixelForDuration():
    # Add the duration to the current time
    duration = int(input("Please enter a duration: "))
    expires = int(time.time()) + duration
    lcd.clear()
    lcd.show
    return expires
    # Check current time against set expiry


def randomPixelDisplay(expires=showPixelForDuration()):
    while expires >= int(time.time()):
        lcd.set_pixel(random.randint(1, 127), random.randint(1, 63), 1)
        lcd.show()
        time.sleep(2)
        lcd.clear()
        lcd.show()
        lcd.clear()
        lcd.show()


# 5. this function clears the backlight by resetting the rgb to zero
def clearBacklight():
    lcd.clear()
    lcd.show()
    backlight.set_all(0, 0, 0)
    backlight.show()


# Menu Function
def menu():
    choice = 0
    while choice == 0:
        print("""This menu gives you the option to display a vertical and horizontal line, a 
        staircase, clear the backlight and display random pixels on the screen.
        Press Ctrl+C or select "Exit" to exit.
        """)

        print('''
Hello, Please Select a function to execute:
1 - Vertical Line
2 - Horizontal Line
3 - Staircase
4 - Random Pixel
5 - Backlight
6 - Exit
''')
        choice = int(input())  # Gets users input

        if choice == 1:
            verticalDisplay()

        if choice == 2:
            horizontalDisplay()

        if choice == 3:
            callAllFunctionSteps()

        if choice == 4:
            randomPixelDisplay()

        if choice == 5:
            clearBacklight()

        if choice == 6:
            sys.exit(0)


menu()
