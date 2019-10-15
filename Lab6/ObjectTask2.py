import time
from gfxhat import lcd

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

f1 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
pm = [[0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
      [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
      [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
      [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0]
      ]


# get user input for x
def getUserInputX():
    x1 = int(input('please enter a number between 0 and 127: '))
    return x1


# ges user input for y

def getUserInputY():
    y1 = int(input('Please enter a number between 0 and 63: '))
    return y1


# calls the user input functions above, and takes the list parameters
# a delay time is set

def displayObject1(obj, x=getUserInputX(), y=getUserInputY()):
    # if obj is None:
    #     obj = f1
    for row in obj:
        y += 1
        for state in row:
            x += 1
            lcd.set_pixel(x, y, state)
            lcd.show()
            time.sleep(0.1)
        lcd.show()
        x = 0


clearScreen()
backLight()
displayObject1(pm)

lcd.show()

clearScreen()
backLight()

time.sleep(1)
displayObject1(f1)
