# This program draws staircases on the GFXHat


from gfxhat import lcd

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


callAllFunctionSteps()

# this shows the output to the screen
lcd.show()
