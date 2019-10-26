import time
import random
from gfxhat import lcd, backlight, fonts
from math import pi
from math import sqrt
import math
from PIL import Image, ImageFont, ImageDraw


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


# clearscreen of gfxhat
def ClearScreen():
    lcd.clear()
    lcd.show()
    backlight.set_all(200, 200, 200)
    backlight.show()


def clearBacklight():
    backlight.set_all(0, 0, 0)
    backlight.show()


def setBacklight():
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    backlight.set_all(r, g, b)
    backlight.show()
