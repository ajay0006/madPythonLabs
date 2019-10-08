import random
import gfxhat
import time
import signal
from gfxhat import lcd
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

lcd.clear()
lcd.show()


def generateRandomX():
    for x in range(1):
        randX = random.randint(1, 127)
    return randX


def generateRandomY():
    for x in range(1):
        randY = random.randint(1, 63)
    return randY


lcd.set_pixel(generateRandomX(), generateRandomY(), 1)
# touch.set_repeat_rate(120)
time.sleep(5)

# touch.set_repeat_rate(120)

lcd.show()
