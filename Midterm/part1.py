#!/usr/bin/env python

import time, click
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

f1South = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

f1Erase = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]


def rotateObject(obj):
    rotated_image = [[] for x in range(len(obj))]
    for i in range(len(obj)):
        for j in range(len(obj[i])):
            rotated_image[len(obj) - j - 1].append(obj[i][j])
    return rotated_image


def verticalSegmentS(xVS=0, yVS=0, hVS=5):
    for i in range(0, 63):
        xVS = xVS + 1
        yVS = yVS + hVS
        if y == 63:
            break
        lcd.set_pixel(x, y, 1)
        lcd.show()


def horizontalSegmentS(xHS=0, yHS=0, wHS=5):
    for i in range(0, 63):
        xHS = xHS + wHS
        yHS = yHS + 1
        if x == 127:
            break
        lcd.set_pixel(xHS, yHS, 1)
        lcd.show()


def displayObject(obj, x, y):
    i = 0
    for line in obj:
        j = 0
        for pixel in line:
            lcd.set_pixel(x + j, y + i, pixel)
            j = j + 1
        i = i + 1
    lcd.show()


def moveObject(obj, x, y, vx, vy):
    x = x + vx
    y = y + vy

    i = 0
    for line in obj:
        j = 0
        for pixel in line:
            lcd.set_pixel(x + j, y + i, pixel)
            j = j + 1
        i = i + 1
    lcd.show()


#
#
def eraseObject(obj, x, y):
    i = 0
    for line in obj:
        j = 0
        for pixel in line:
            lcd.set_pixel(x + j, y + i, pixel)
            j = j + 1
        i = i + 1
    lcd.show()


def clearScreen(lcd):
    lcd.clear()
    lcd.show()


def displayText(text, lcd, x, y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 38)
    w, h = font.getsize(text)
    draw.text((x, y), text, 1, font)
    for x1 in range(x, x + w):
        for y1 in range(y, y + h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()


def eraseText(text, lcd, x, y):
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 38)
    w, h = font.getsize(text)
    draw.text((x, y), text, 1, font)
    for x1 in range(x, x + w):
        for y1 in range(y, y + h):
            lcd.set_pixel(x1, y1, 0)
    lcd.show()


clearScreen(lcd)
backlight.set_all(0, 255, 0)
backlight.show()
displayText("Spaceship", lcd, 25, 1)
time.sleep(2)
eraseText("Spaceship", lcd, 25, 1)

f1East = rotateObject(f1South)
f1North = rotateObject(f1East)
f1West = rotateObject(f1North)

x = y = 0
w = h = 8
vx = vy = 3
f1 = f1South
displayObject(f1, x, y)

quit = False
while not quit:
    c = click.getchar()

    # Erase Everything
    eraseObject(f1Erase, x, y)

    # Move everything
    if c == 'q':
        quit = True

    elif c == '\x1b[A':  # up
        f1 = f1North
        y = y - vy

    elif c == '\x1b[B':  # down
        f1 = f1South
        y = y + vy

    elif c == '\x1b[C':  # right
        f1 = f1East
        x = x + vx

    elif c == '\x1b[D':  # left
        f1 = f1West
        x = x - vx

    # Collision Detection
    if y < 0 or y + h > 63 or x + w > 127 or x < 0:
        displayText("Ouch Boom", lcd, 5, 1)
        time.sleep(0.4)
        eraseText("Ouch Boom", lcd, 5, 1)
        if y < 0: y = 0
        if y + h > 63: y = 63 - h
        if x < 0: x = 0
        if x + w > 127: x = 127 - w

    # Display Everything
    displayObject(f1, x, y)

backlight.set_all(0, 0, 0)
backlight.show()
lcd.clear()
lcd.show()
