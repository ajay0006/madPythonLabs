# this code displays a vertical line across the gfx hat screen
from gfxhat import lcd

lcd.clear()
lcd.show()


# this is a function that takes the user input for the X coordinate and validates it, making sure it isnt above 127
# it also returns the users input

def verticalDisplayInput():
    x = int(input("please enter a value less than 128: "))
    if x > 127:
        print("you have entered a number greater than 127")
        x = int(input("please enter a value less than 128: "))
    while x <= 128:
        return x


# this function sets the coordinates for the y axis that prints the horizontal line

def verticalDisplay(x=verticalDisplayInput(), y=1):
    while y <= 63:
        lcd.set_pixel(x, y, 1)
        y = y + 1


# the function is called and the line is displayed
verticalDisplay()
lcd.show()
