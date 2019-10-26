# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Damilola Ajayi >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 040984692 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import time
import random
from gfxhat import lcd, backlight, fonts
from math import pi
from math import sqrt
import math
from PIL import Image, ImageFont, ImageDraw


# ............................. GFXHAT related ......................................

# clears the screen
def ClearScreen():
    lcd.clear()
    lcd.show()


# clears the backlight
def clearBacklight():
    backlight.set_all(0, 0, 0)
    backlight.show()


# sets the backlight to a random color
def setBacklight():
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    backlight.set_all(r, g, b)
    backlight.show()


# <>>>>>>>>>>>>>>>>>>>>>>>>>>> GFXHAT related end>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ...................................Lab3 related ..............................................................
# Function for area of circle
def areaOfCircle(radius):
    area = pi * radius ** 2
    return area


# Function for MPG
def mpg(miles, gallon):
    mileage = int(miles) / int(gallon)
    return mileage


# Function for temperature conversion
def celsiusToFahrenheit(celsius):
    fahrenheit = float(float(celsius) * (9 / 5)) + 32
    return fahrenheit


# Function for distance between two points
def calDistBtwPoints(x1, x2, y1, y2):
    if (x2 < x1) or (y2 < y1):
        exit("please enter valid variables")
    else:
        a = x2 - x1
        b = y2 - y1
        d = sqrt(pow(a, 2) * pow(b, 2))
        return d


# <>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Lab 3 End >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ................................Lab5 related...............................................................

# this function sets the coordinates for the y axis that prints the horizontal line

def horizontalDisplay(y, x=1):
    while x <= 127:
        lcd.set_pixel(x, y, 1)
        x = x + 1


# this function sets the coordinates for the y axis that prints the horizontal line

def verticalDisplay(x, y=1):
    while y <= 63:
        lcd.set_pixel(x, y, 1)
        y = y + 1


# this function adds the duration set by the user in ms to the time real time counter
# this is so that no matter what time the program is run it will clear
def show_pixel_for_duration(duration):
    # Add the duration to the current time
    expires = int(time.time()) + duration
    lcd.clear()
    lcd.show()
    # Check current time against set expiry

    while expires >= int(time.time()):
        lcd.set_pixel(random.randint(1, 127), random.randint(1, 63), 1)
        lcd.show()
        time.sleep(2)
        lcd.clear()
        lcd.show()
    lcd.clear()
    lcd.show()


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


# <>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Lab 5 Related End >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# .............................................. Lab 6 Related ..............................................


# DISPLAYS THE ETCH A SKETCH SCREEN ACROSS THE THE DISPLAY SCREEN AT A POSITION SET
def displayText(text, x=20, y=15):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x, y), text, 1, font)
    for x1 in range(x, x + w):
        for y1 in range(y, y + h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()


# THIS FUNCTION GETS THE CHARACTER CODE FOR WHICHEVER ARROW KEYS IS HIT BY THE USER AND CALLS THE SUBSEQUENT FUNCTION
# THAT RELATES TO THAT ARROW KEY CHARACTER CODE

def arrowKeyPressed():
    char = getchar()
    if char == '\x1b[A':
        upArrowPressed(char)
    elif char == '\x1b[B':
        downArrowPressed(char)
    elif char == '\x1b[C':
        rightArrowPressed(char)
    elif char == '\x1b[D':
        leftArrowPressed(char)
    elif char == 's':
        clearScreen()
    elif char == 'q':
        exit()


# THIS IS THE FUNCTION FOR THE UP ARROW KEY, THIS FUNCTION PRINTS TRAILING PIXELS ON THE GFX DISPLAY EACH TIME THE
# ARROW KEY IS HIT.
# IT ENSURES THAT THE PIXELS DRAWN DO NOT PASS THE RESOLUTION DISPLAY BOUNDARY OF THE GFXHAT
# IF A DIFFERENT ARROW KEY IS HIT THAT DOESNT CORRESPOND TO THE "UP" ARROW KEY, THE FUNCTION THAT RELATES TO THAT
# ARROW KEY IS CALLED


def upArrowPressed(up, xup, yup):
    print(up)
    print(xup)
    print('first up arrow', yup)
    while up == '\x1b[A':
        up = getchar()
        print('second up arrow', yup)
        if yup <= 63:
            yup -= 1
            lcd.set_pixel(xup, yup, 1)
            print('third up arrow', yup)
            lcd.show()
        if yup == 0:
            print('fourth up arrow', yup)
            yup = 63
            # yup -= 1
            print('fifth up arrow', yup)
            lcd.set_pixel(xup, yup, 1)
            lcd.show()

        if up == '\x1b[C':
            rightArrowPressed(up, xup, yup)
        if up == '\x1b[B':
            downArrowPressed(up, xup, yup)
        if up == '\x1b[D':
            leftArrowPressed(up, xup, yup)
        else:
            pass


# THIS IS THE FUNCTION FOR THE DOWN ARROW KEY, THIS FUNCTION PRINTS TRAILING PIXELS ON THE GFX DISPLAY EACH TIME THE
# ARROW KEY IS HIT.
# IT ENSURES THAT THE PIXELS DRAWN DO NOT PASS THE RESOLUTION DISPLAY BOUNDARY OF THE GFXHAT
# IF A DIFFERENT ARROW KEY IS HIT THAT DOESNT CORRESPOND TO THE "DOWN" ARROW KEY, THE FUNCTION THAT RELATES TO THAT
# ARROW KEY IS CALLED


def downArrowPressed(down, xDown, yDown):
    print(down)
    print(xDown)
    print('first down arrow', yDown)
    while down == '\x1b[B':
        down = getchar()
        print('second down arrow', yDown)
        if yDown == 63:
            print('third down arrow', yDown)
            yDown = 0
            yDown += 1
            print('fourth down arrow', yDown)
            lcd.set_pixel(xDown, yDown, 1)
            lcd.show()

        if yDown >= 0:
            yDown += 1
            lcd.set_pixel(xDown, yDown, 1)

            print('fifth down arrow', yDown)
            lcd.show()
        if down == '\x1b[C':
            rightArrowPressed(down, xDown, yDown)
        if down == '\x1b[A':
            upArrowPressed(down, xDown, yDown)
        if down == '\x1b[D':
            leftArrowPressed(down, xDown, yDown)
        else:
            pass


# THIS IS THE FUNCTION FOR THE RIGHT ARROW KEY, THIS FUNCTION PRINTS TRAILING PIXELS ON THE GFX DISPLAY EACH TIME THE
# ARROW KEY IS HIT.
# IT ENSURES THAT THE PIXELS DRAWN DO NOT PASS THE RESOLUTION DISPLAY BOUNDARY OF THE GFXHAT
# IF A DIFFERENT ARROW KEY IS HIT THAT DOESNT CORRESPOND TO THE "RIGHT" ARROW KEY, THE FUNCTION THAT RELATES TO THAT
# ARROW KEY IS CALLED


def rightArrowPressed(right, xRight, yRight):
    print(right)
    print(yRight)
    print('first right arrow', xRight)
    while right == '\x1b[C':
        right = getchar()
        print('second right arrow', xRight)
        if xRight >= 0:
            xRight += 1
            lcd.set_pixel(xRight, yRight, 1)

            print('third right arrow', xRight)
            lcd.show()
        if xRight == 127:
            print('fourth right arrow', xRight)
            xRight = 0
            xRight += 1
            print('fifth right arrow', xRight)
            lcd.set_pixel(xRight, yRight, 1)

            lcd.show()
        if right == '\x1b[A':
            upArrowPressed(right, xRight, yRight)
        if right == '\x1b[B':
            downArrowPressed(right, xRight, yRight)
        if right == '\x1b[D':
            leftArrowPressed(right, xRight, yRight)
        else:
            pass


# THIS IS THE FUNCTION FOR THE LEFT ARROW KEY, THIS FUNCTION PRINTS TRAILING PIXELS ON THE GFX DISPLAY EACH TIME THE
# ARROW KEY IS HIT.
# IT ENSURES THAT THE PIXELS DRAWN DO NOT PASS THE RESOLUTION DISPLAY BOUNDARY OF THE GFXHAT
# IF A DIFFERENT ARROW KEY IS HIT THAT DOESNT CORRESPOND TO THE "LEFT" ARROW KEY, THE FUNCTION THAT RELATES TO THAT
# ARROW KEY IS CALLED


def leftArrowPressed(left, xLeft, yLeft):
    print(left)
    print(yLeft)
    print('first left arrow', xLeft)
    while left == '\x1b[D':
        left = getchar()
        print('second left arrow', xLeft)
        if xLeft == 0:
            print('fourth right arrow', xLeft)
            xLeft = 127
            xLeft -= 1
            print('fifth right arrow', xLeft)
            lcd.set_pixel(xLeft, yLeft, 1)
            lcd.show()

        if xLeft >= 1:
            xLeft -= 1
            lcd.set_pixel(xLeft, yLeft, 1)

            print('third right arrow', xLeft)
            lcd.show()
        if left == '\x1b[A':
            upArrowPressed(left, xLeft, yLeft)
        if left == '\x1b[B':
            downArrowPressed(left, xLeft, yLeft)
        if left == '\x1b[C':
            rightArrowPressed(left, xLeft, yLeft)
        else:
            pass


# <>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Lab 6 Related End >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# .............................................. Lab 7 Related ..............................................

eraseBall = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
# this function transverses the array vertically and horizontally, converts 0's & 1's to pixels that are displayed on
#  the gfxhat


def eraseObject1(obj, xErase, yErase):
    i = 0
    for line in obj:
        j = 0
        for pixel in line:
            lcd.set_pixel(xErase + j, yErase + i, pixel)
            j = j + 1
        i = i + 1
    time.sleep(1)
    lcd.show()


# this function transverses the array vertically and horizontally, converts 0's & 1's to pixels that are displayed on
#  the gfxhat
def moveObject(obj, xMove, yMove):
    i = 0
    for line in obj:
        j = 0
        for pixel in line:
            lcd.set_pixel(xMove + j, yMove + i, pixel)
            j = j + 1
        i = i + 1
        lcd.show()


# this function takes the obj parameter, x & y start positions, variations in x & y speed and constants which represent
# the display boundaries on the gfx hat
def checkCollision(obj, xLoop, yLoop, dx=10, dy=10, Sx=128, Sy=64):
    # length and width of the array are assigned to variables, making it easier to type
    width = len(obj[0])
    height = len(obj)
    # the boundary checker loop
    while True:
        if 0 < (xLoop + width) <= Sx:
            # +ve increment in both x an y
            # print('x:{} y:{} 1a'.format(xLoop, yLoop))
            xLoop += dx
            yLoop += dy
            # print('x:{} y:{} 1b'.format(xLoop, yLoop))
            if yLoop < 0:
                # returns a positive value for the y coordinate
                yLoop = yLoop + abs(yLoop)
                dy = abs(dy)
        if (yLoop + height) > Sy:
            # print('x:{} y:{} 2a'.format(xLoop, yLoop))
            # ensures that the increment is +ve
            dy = -abs(dy)
            yLoop += dy
            # print('x:{} y:{} 2b'.format(xLoop, yLoop))
            if xLoop < 0:
                # print('x:{} y:{} 2c'.format(xLoop, yLoop))
                # converts the x coordinate to a positive value
                xLoop = xLoop + abs(xLoop)
                # converts the increment on the x-axis to a positive value
                dx = abs(dx)
                # print('x:{} y:{} 2d'.format(xLoop, yLoop))
        if (xLoop + width) > Sx:
            # print('x:{} y:{} 3a'.format(xLoop, yLoop))
            # converts the increment on the x-axis to a negative value so it decrements
            dx = -abs(dx)
            xLoop += dx
            # yLoop += dy
            # print('x:{} y:{} 3b'.format(xLoop, yLoop))
        if yLoop <= 0:
            # print('x:{} y:{} 4a'.format(xLoop, yLoop))
            # converts the increment on the y-axis to a positive value
            dy = abs(dy)
            yLoop += dy
            # xLoop += dx
            print('x:{} y:{} 4b'.format(xLoop, yLoop))
        if xLoop < 0:
            print('x:{} y:{} 5a'.format(xLoop, yLoop))
            dx = abs(dx)
            # resets the increment to +ve value
            xLoop += dx
            # yLoop += dy
            print('x:{} y:{} 5b'.format(xLoop, yLoop))
        #     calls the move and erase object functions and passes the values from the loop one at a time
        moveObject(obj, xLoop, yLoop)
        eraseObject1(eraseBall, xLoop, yLoop)
