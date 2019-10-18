import time
import random
from gfxhat import lcd, backlight, fonts
import math
from PIL import Image, ImageFont, ImageDraw


def ClearScreen():
    lcd.clear()
    lcd.show()
