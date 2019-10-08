import time
import random
import gfxhat
import signal
from gfxhat import lcd
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw


# this function adds the duration set by the user in ms to the time real time counter
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


randomPixelDisplay()
