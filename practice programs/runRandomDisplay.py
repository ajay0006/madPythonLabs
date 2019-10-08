import time
import random
import gfxhat
import signal
from gfxhat import lcd
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw


def show_pixel_static_for_countdown(duration):
    """ This function just shows a random pixel statically
    for the duration you want.
    """
    lcd.set_pixel(random.randint(1, 127), random.randint(1, 63), 1)
    touch.set_repeat_rate(120)
    time.sleep(duration)


show_pixel_static_for_countdown(5)
