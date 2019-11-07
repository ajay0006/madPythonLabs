import time
import random
from gfxhat import lcd, backlight, fonts
from math import pi
from math import sqrt
import math
from PIL import Image, ImageFont, ImageDraw

x = 20
y = 20


def southLine(xSouth, ySouth, h):
    print('Drawing...')
    while 63 > ySouth >= 0:
        for i in range(0, h):
            ySouth = ySouth + 1
            if ySouth > 63:
                break
            lcd.set_pixel(xSouth, ySouth, 1)
            lcd.show()


def eastLine(xEast, yEast, h):
    print('Drawing...')
    while 127 > xEast >= 0:
        for i in range(0, h):
            xEast = xEast + 1
            if xEast > 127:
                break
            lcd.set_pixel(xEast, yEast, 1)
            lcd.show()


def drawSquare(xSquare, ySquare, side):
    a = xSquare
    b = ySquare
    z = xSquare + side
    zz = ySquare + side
    for i in range(0, side):
        xSquare += 1
        print(xSquare, 'first')
        if xSquare > z:
            break
        lcd.set_pixel(xSquare, ySquare, 1)
    for j in range(0, side):
        ySquare += 1
        if ySquare > zz:
            break
        lcd.set_pixel(xSquare, ySquare, 1)
        print(xSquare, ySquare, 'display')
    for k in range(0, side):
        xSquare -= 1
        if xSquare < a:
            break
        lcd.set_pixel(xSquare, ySquare, 1)

    for l in range(0, side):
        ySquare -= 1
        if ySquare < b:
            break
        lcd.set_pixel(xSquare, ySquare, 1)
    lcd.show()


def horizontalLine(xHor, yHor, length):
    for i in range(0, length):
        xHor = xHor - 1
        yHor = yHor - 1
        if xHor == (xHor - length):
            break
        lcd.set_pixel(x, y, 1)
        lcd.show()

    # for i in range(0, length):
    #     y = y - d
    #     if y == (y - length):
    #         break
    #     lcd.set_pixel(x, y, 1)
    #     lcd.show()


def drawDiamond(xD, yD, d=12):
    xFirst = xD
    yFirst = yD
    aRight = xD + d
    aLeft = xD - d
    b = yD + (d * 2)
    bLeft = yD + d
    bRight = yD - d
    while (xD > 7) and (yD < bLeft):
        xD -= 1
        yD += 1
        print(xD, yD, "x and y pixel 1")
        lcd.set_pixel(xD, yD, 1)
        lcd.show()
    while (xD < xFirst) and (yD < b):
        xD += 1
        yD += 1
        print(xD, yD, "x and y pixel 2")
        lcd.set_pixel(xD, yD, 1)
        lcd.show()
    while (xD < aRight) and (yD > bRight):
        xD += 1
        yD -= 1
        print(xD, yD, "x and y pixel 3")
        lcd.set_pixel(xD, yD, 1)
        lcd.show()
    while (xD > xFirst) and (yD > yFirst):
        xD -= 1
        yD -= 1
        print(xD, yD, "x and y pixel 3")
        lcd.set_pixel(xD, yD, 1)
        lcd.show()
        if (xD == xFirst) and (yD == yFirst):
            break


def setBackLight():
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    backlight.set_all(r, g, b)
    backlight.show()


setBackLight()
drawDiamond(x, y)

# southLine(x, y, 16)
# eastLine(x, y, 16)

lcd.clear()
lcd.show()
time.sleep(1)
drawSquare(34, 5, 12)

# horizontalLine(20, 20, 16)
