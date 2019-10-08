from gfxhat import touch, lcd, backlight, fonts

# this function clears the backlight by resetting the rgb to zero
def clearBacklight():
    lcd.clear()
    lcd.show()
    backlight.set_all(0, 0, 0)
    backlight.show()


clearBacklight()
