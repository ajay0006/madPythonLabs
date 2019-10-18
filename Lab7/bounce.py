from gfxhat import lcd, backlight
import time


# this sets the backlight color so the pixels are visible

def backLight():
    backlight.set_all(125, 78, 95)
    backlight.show()


#  this clears the screen of any pixels
def clearScreen():
    lcd.clear()
    lcd.show()


# lists

ball = [
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0]
]


# get user input for x
def getUserInputBounceX():
    xStart = int(input('please enter a number between 0 and 127: '))
    return xStart


# ges user input for y

def getUserInputBounceY():
    yStart = int(input('Please enter a number between 0 and 63: '))
    return yStart


# calls the user input functions above, and takes the list parameters
# a delay time is set

def displayObject1(obj, x1=getUserInputBounceX(), y1=getUserInputBounceY()):
    # if obj is None:
    #     obj = f1
    for row in obj:
        y1 += 1
        for state in row:
            x1 += 1
            lcd.set_pixel(x1, y1, state)
            lcd.show()
            time.sleep(0.1)
        lcd.show()
        x1 = 0


def eraseObject1(obj, x1=getUserInputBounceX(), y1=getUserInputBounceY()):
    # if obj is None:
    #     obj = f1
    for row in obj:
        y1 -= 1
        for state in row:
            x1 -= 1
            lcd.set_pixel(x1, y1, state)
            lcd.show()
            time.sleep(0)
        lcd.show()
        x1 = 1


clearScreen()
backLight()
displayObject1(ball)

lcd.show()
