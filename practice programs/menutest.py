import time
import sys
import atexit

from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

print("""This menu gives you the option to display a vertical and horizontal line, a 
staircase, clear the backlight and display random pixels on the screen.
Press Ctrl+C or select "Exit" to exit.
""")


# 1. this is the vertical line display validation, ensuring parameters do not cause an error
def verticalDisplayInput():
    x2 = int(input("please enter a value less than 128: "))
    if x2 > 127:
        print("you have entered a number greater than 127")
        x2 = int(input("please enter a value less than 128: "))
    while x2 <= 128:
        return x2


# this function sets the coordinates for the y axis that prints the horizontal line, after validation
# must have passed above

def verticalDisplay(x2=verticalDisplayInput(), y2=1):
    while y2 <= 63:
        lcd.set_pixel(x2, y2, 1)
        y2 = y2 + 1


# 2. this is the horizontal line function, where the user input is first validated
def horizontalDisplayInput():
    y1 = int(input("please enter a value less than 63: "))
    if y1 > 63:
        print("you have entered a number greater than 63")
        y1 = int(input("please enter a value less than 63: "))
    while y1 <= 63:
        return y1


# this function sets the coordinates for the y axis that prints the horizontal line after
# validation has been done in the function above

def horizontalDisplay(y1=horizontalDisplayInput(), x1=1):
    while x1 <= 127:
        lcd.set_pixel(x1, y1, 1)
        x1 = x1 + 1


width, height = lcd.dimensions()

# A squarer pixel font
# font = ImageFont.truetype(fonts.BitocraFull, 11)

# A slightly rounded, Ubuntu-inspired version of Bitocra
font = ImageFont.truetype(fonts.BitbuntuFull, 10)

image = Image.new('P', (width, height))

draw = ImageDraw.Draw(image)


class MenuOption:
    def __init__(self, name, action, options=()):
        self.name = name
        self.action = action
        self.options = options
        self.size = font.getsize(name)
        self.width, self.height = self.size

    def trigger(self):
        self.action(*self.options)


def set_backlight(r, g, b):
    backlight.set_all(r, g, b)
    backlight.show()


menu_options = [
    MenuOption('Vertical Line', verticalDisplay()),
    MenuOption('Horizontal Line', horizontalDisplay()),
    MenuOption('Staircase Display', set_backlight, (0, 0, 255)),
    MenuOption('Random Pixel Display', set_backlight, (255, 0, 255)),
    MenuOption('Clear Backlight', set_backlight, (255, 255, 255)),
    MenuOption('Exit', sys.exit, (0,))
]

current_menu_option = 1

trigger_action = False


def handler(ch, event):
    global current_menu_option, trigger_action
    if event != 'press':
        return
    if ch == 1:
        current_menu_option += 1
    if ch == 0:
        current_menu_option -= 1
    if ch == 4:
        trigger_action = True
    current_menu_option %= len(menu_options)


for x in range(6):
    touch.set_led(x, 0)
    backlight.set_pixel(x, 255, 255, 255)
    touch.on(x, handler)

backlight.show()


def cleanup():
    backlight.set_all(0, 0, 0)
    backlight.show()
    lcd.clear()
    lcd.show()


atexit.register(cleanup)

try:
    while True:
        image.paste(0, (0, 0, width, height))
        offset_top = 0

        if trigger_action:
            menu_options[current_menu_option].trigger()
            trigger_action = False

        for index in range(len(menu_options)):
            if index == current_menu_option:
                break
            offset_top += 12

        for index in range(len(menu_options)):
            x = 10
            y = (index * 12) + (height / 2) - 4 - offset_top
            option = menu_options[index]
            if index == current_menu_option:
                draw.rectangle(((x - 2, y - 1), (width, y + 10)), 1)
            draw.text((x, y), option.name, 0 if index == current_menu_option else 1, font)

        w, h = font.getsize('>')
        draw.text((0, (height - h) / 2), '>', 1, font)

        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x, y))
                lcd.set_pixel(x, y, pixel)

        lcd.show()
        time.sleep(1.0 / 30)

except KeyboardInterrupt:
    cleanup()
