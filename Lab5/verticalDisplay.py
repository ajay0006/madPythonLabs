from gfxhat import lcd

lcd.clear()
lcd.show()


def verticalDisplay(x):
    y = 1
    while y <= 63:
        lcd.set_pixel(x, y, 1)
        y = y + 1


b = int(input('please input a X value for the vertical line: '))
verticalDisplay(b)
lcd.show()
