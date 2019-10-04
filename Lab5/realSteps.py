import gfxhat
import time
import signal
from gfxhat import lcd
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

lcd.clear()
lcd.show()


def firstStep():
    for x in range(0, 21):
        lcd.set_pixel(x, 60, 1)


def secondStep():
    for y in range(60, 51, -1):
        lcd.set_pixel(20, y, 1)


def thirdStep():
    for x in range(20, 41):
        lcd.set_pixel(x, 51, 1)


def fourthStep():
    for y in range(50, 41, -1):
        lcd.set_pixel(40, y, 1)


def fifthStep():
    for x in range(40, 61):
        lcd.set_pixel(x, 41, 1)


def sixthStep():
    for y in range(40, 31, -1):
        lcd.set_pixel(60, y, 1)


def seventhStep():
    for x in range(60, 81):
        lcd.set_pixel(x, 31, 1)


def eightStep():
    for y in range(30, 21, -1):
        lcd.set_pixel(80, y, 1)


def ninthStep():
    for x in range(80, 101):
        lcd.set_pixel(x, 21, 1)


def tenthStep():
    for y in range(20, 11, -1):
        lcd.set_pixel(100, y, 1)


def eleventhStep():
    for x in range(100, 121):
        lcd.set_pixel(x, 11, 1)


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
lcd.show()
