import ajay0006Lib as Dj

ball = [
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0]
]


Dj.ClearScreen()
Dj.setBacklight()

# get user input for x
xStart = int(input('please enter a number between 0 and 127: '))

# ges user input for y
yStart = int(input('Please enter a number between 0 and 63: '))

Dj.checkCollision(ball, xStart, yStart)
