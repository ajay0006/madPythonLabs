# this code displays a horizontal line across the gfx hat screen
from gfxhat import lcd

lcd.clear()
lcd.show()


# this is a function that takes the user input for the y coordinate and validates it, making sure it isnt above 63
# it also returns the users input

def horizontalDisplayInput():
    y = int(input("please enter a value less than 63: "))
    if y > 63:
        print("you have entered a number greater than 63")
        y = int(input("please enter a value less than 63: "))
    while y <= 63:
        return y


# this function sets the coordinates for the y axis that prints the horizontal line

def horizontalDisplay(y=horizontalDisplayInput(), x=1):
    while x <= 127:
        lcd.set_pixel(x, y, 1)
        x = x + 1


# the function is called and the line is displayed

horizontalDisplay()
lcd.show()
