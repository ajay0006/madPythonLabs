import gfxhat
import time
import signal
from gfxhat import lcd
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

lcd.clear()
lcd.show()


def horizontalDisplay(y):
    x = 1
    while x <= 127:
        lcd.set_pixel(x, y, 1)
        x = x + 1


b = int(input('please input a y value for the vertical line: '))
horizontalDisplay(b)
lcd.show()
