import click
from gfxhat import lcd, fonts
from PIL import Image, ImageFont, ImageDraw
from click import getchar
from gfxhat import backlight

lcd.clear()
lcd.show()

x2 = 0
y2 = 63


# text = "Etch a Sketch"

#
def clearScreen():
    lcd.clear()
    lcd.show()


# this sets the backlight color so the pixels are visible
def backLight():
    backlight.set_all(145, 34, 108)
    backlight.show()


# DISPLAYS THE ETCH A SKETCH SCREEN ACROSS THE THE DISPLAY SCREEN AT A POSITION SET
def displayText(text, x=20, y=15):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x, y), text, 1, font)
    for x1 in range(x, x + w):
        for y1 in range(y, y + h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()


# THIS FUNCTION GETS THE CHARACTER CODE FOR WHICHEVER ARROW KEYS IS HIT BY THE USER AND CALLS THE SUBSEQUENT FUNCTION
# THAT RELATES TO THAT ARROW KEY CHARACTER CODE

def arrowKeyPressed():
    char = getchar()
    if char == '\x1b[A':
        upArrowPressed(char)
    elif char == '\x1b[B':
        downArrowPressed(char)
    elif char == '\x1b[C':
        rightArrowPressed(char)
    elif char == '\x1b[D':
        leftArrowPressed(char)
    elif char == 's':
        clearScreen()
    elif char == 'q':
        exit()


# THIS IS THE FUNCTION FOR THE UP ARROW KEY, THIS FUNCTION PRINTS TRAILING PIXELS ON THE GFX DISPLAY EACH TIME THE
# ARROW KEY IS HIT.
# IT ENSURES THAT THE PIXELS DRAWN DO NOT PASS THE RESOLUTION DISPLAY BOUNDARY OF THE GFXHAT
# IF A DIFFERENT ARROW KEY IS HIT THAT DOESNT CORRESPOND TO THE "UP" ARROW KEY, THE FUNCTION THAT RELATES TO THAT
# ARROW KEY IS CALLED


def upArrowPressed(up, xup=x2, yup=y2):
    print(up)
    print(xup)
    print('first up arrow', yup)
    while up == '\x1b[A':
        up = getchar()
        print('second up arrow', yup)
        if yup <= 63:
            yup -= 1
            lcd.set_pixel(xup, yup, 1)
            print('third up arrow', yup)
            lcd.show()
        if yup == 0:
            print('fourth up arrow', yup)
            yup = 63
            # yup -= 1
            print('fifth up arrow', yup)
            lcd.set_pixel(xup, yup, 1)
            lcd.show()

        if up == '\x1b[C':
            rightArrowPressed(up, xup, yup)
        if up == '\x1b[B':
            downArrowPressed(up, xup, yup)
        if up == '\x1b[D':
            leftArrowPressed(up, xup, yup)
        else:
            pass


# THIS IS THE FUNCTION FOR THE DOWN ARROW KEY, THIS FUNCTION PRINTS TRAILING PIXELS ON THE GFX DISPLAY EACH TIME THE
# ARROW KEY IS HIT.
# IT ENSURES THAT THE PIXELS DRAWN DO NOT PASS THE RESOLUTION DISPLAY BOUNDARY OF THE GFXHAT
# IF A DIFFERENT ARROW KEY IS HIT THAT DOESNT CORRESPOND TO THE "DOWN" ARROW KEY, THE FUNCTION THAT RELATES TO THAT
# ARROW KEY IS CALLED


def downArrowPressed(down, xDown=x2, yDown=y2):
    print(down)
    print(xDown)
    print('first down arrow', yDown)
    while down == '\x1b[B':
        down = getchar()
        print('second down arrow', yDown)
        if yDown == 63:
            print('third down arrow', yDown)
            yDown = 0
            yDown += 1
            print('fourth down arrow', yDown)
            lcd.set_pixel(xDown, yDown, 1)
            lcd.show()

        if yDown >= 0:
            yDown += 1
            lcd.set_pixel(xDown, yDown, 1)

            print('fifth down arrow', yDown)
            lcd.show()
        if down == '\x1b[C':
            rightArrowPressed(down, xDown, yDown)
        if down == '\x1b[A':
            upArrowPressed(down, xDown, yDown)
        if down == '\x1b[D':
            leftArrowPressed(down, xDown, yDown)
        else:
            pass


# THIS IS THE FUNCTION FOR THE RIGHT ARROW KEY, THIS FUNCTION PRINTS TRAILING PIXELS ON THE GFX DISPLAY EACH TIME THE
# ARROW KEY IS HIT.
# IT ENSURES THAT THE PIXELS DRAWN DO NOT PASS THE RESOLUTION DISPLAY BOUNDARY OF THE GFXHAT
# IF A DIFFERENT ARROW KEY IS HIT THAT DOESNT CORRESPOND TO THE "RIGHT" ARROW KEY, THE FUNCTION THAT RELATES TO THAT
# ARROW KEY IS CALLED


def rightArrowPressed(right, xRight=x2, yRight=y2):
    print(right)
    print(yRight)
    print('first right arrow', xRight)
    while right == '\x1b[C':
        right = getchar()
        print('second right arrow', xRight)
        if xRight >= 0:
            xRight += 1
            lcd.set_pixel(xRight, yRight, 1)

            print('third right arrow', xRight)
            lcd.show()
        if xRight == 127:
            print('fourth right arrow', xRight)
            xRight = 0
            xRight += 1
            print('fifth right arrow', xRight)
            lcd.set_pixel(xRight, yRight, 1)

            lcd.show()
        if right == '\x1b[A':
            upArrowPressed(right, xRight, yRight)
        if right == '\x1b[B':
            downArrowPressed(right, xRight, yRight)
        if right == '\x1b[D':
            leftArrowPressed(right, xRight, yRight)
        else:
            pass


# THIS IS THE FUNCTION FOR THE LEFT ARROW KEY, THIS FUNCTION PRINTS TRAILING PIXELS ON THE GFX DISPLAY EACH TIME THE
# ARROW KEY IS HIT.
# IT ENSURES THAT THE PIXELS DRAWN DO NOT PASS THE RESOLUTION DISPLAY BOUNDARY OF THE GFXHAT
# IF A DIFFERENT ARROW KEY IS HIT THAT DOESNT CORRESPOND TO THE "LEFT" ARROW KEY, THE FUNCTION THAT RELATES TO THAT
# ARROW KEY IS CALLED


def leftArrowPressed(left, xLeft=x2, yLeft=y2):
    print(left)
    print(yLeft)
    print('first left arrow', xLeft)
    while left == '\x1b[D':
        left = getchar()
        print('second left arrow', xLeft)
        if xLeft == 0:
            print('fourth right arrow', xLeft)
            xLeft = 127
            xLeft -= 1
            print('fifth right arrow', xLeft)
            lcd.set_pixel(xLeft, yLeft, 1)
            lcd.show()

        if xLeft >= 1:
            xLeft -= 1
            lcd.set_pixel(xLeft, yLeft, 1)

            print('third right arrow', xLeft)
            lcd.show()
        if left == '\x1b[A':
            upArrowPressed(left, xLeft, yLeft)
        if left == '\x1b[B':
            downArrowPressed(left, xLeft, yLeft)
        if left == '\x1b[C':
            rightArrowPressed(left, xLeft, yLeft)
        else:
            pass


# THE DISPLAY THE ETCH A SKETCH FUNCTION IS CALLED

backLight()
displayText("Etch a Sketch")
backLight()

# THIS CALLS THE FUNCTION THAT GETS THE CHARACTER CODE OF THE ARROW KEYS AND STARTS OF THE PROGRAM
arrowKeyPressed()
