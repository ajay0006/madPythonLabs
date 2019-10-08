import time
import random
import gfxhat
import signal
from gfxhat import lcd
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw


def show_pixel_for_duration(duration):
    """This function sets various random pixels,
    a different one every second for whatever duration
    if you reduce the value in time.sleep, or remove it
    altogether, you can have a rapid pixel flash. Try reducing
    the delay to say 0.1 and see what happens.
    """
    # Add the duration to the current time
    expires = int(time.time()) + duration
    touch.set_repeat_rate(120)
    # Check current time against set expiry
    while expires >= int(time.time()):
        led.set_pixel(random.randint(1, 127), random.randint(1, 63))
        time.sleep(5)


def show_pixel_static_for_countdown(duration):
    """ This function just shows a random pixel statically
    for the duration you want.
    """
    led.set_pixel(random.randint(1, 127), random.randint(1, 63))
    touch.set_repeat_rate(120)
    time.sleep(duration)


show_pixel_for_duration(10)

show_pixel_static_for_countdown(5)
