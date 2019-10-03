from math import pi
from math import sqrt


def printInstructions():
    print("hello")
    print("this program will calculate area of a circle, mpg, celsius to fahrenheit and distance between two points ")
    print("----------------------------------------------------------------------------------------------------------")


# Function for area of circle
def areaOfCircle(radius):
    area = pi * radius ** 2
    return area


# Function for MPG
def mpg(miles, gallon):
    mileage = int(miles) / int(gallon)
    return mileage


# Function for temperature conversion
def celsiusToFahrenheit(celsius):
    fahrenheit = float(float(celsius) * (9 / 5)) + 32
    return fahrenheit


# Function for distance between two points
def calDistBtwPoints(x1, x2, y1, y2):
    if (x2 < x1) or (y2 < y1):
        exit("please enter valid variables")
    else:
        a = x2 - x1
        b = y2 - y1
        d = sqrt(pow(a, 2) * pow(b, 2))
        return d


printInstructions()

# this  calls the function that calculates and displays the result of the area of the circle

r = float(input("please enter the radius of this circle>: "))
Area = areaOfCircle(r)
print("the Area of a circle of radius r = {1} is {0}".format(Area, r))
print("----------------------------------------------------------------------------------------------------------")

# this  calls the function that this calculates and displays the result of the mileage

m = float(input("please how many miles did you travel> "))
g = input("please how many gallons of fuel did you use > ")
mileages = mpg(m, g)
print("you travelled for {0} miles using {1} gallons, you mileage is {2}".format(m, g, mileages))
print("----------------------------------------------------------------------------------------------------------")

#  this  calls the function that calculates and displays the result of the conversion between celsius and fahrenheit

c = float(input("whats the temperature in celsius> "))
fahrenheits = celsiusToFahrenheit(c)
print("Your Temperature is {0}"'\u1D3C'"F".format(fahrenheits))
print("----------------------------------------------------------------------------------------------------------")

#  this calls the function for calculating distance between two points
X = int(input("please enter the first horizontal coordinate> "))
X2 = int(input("please enter the second horizontal coordinate> "))
Y = int(input("please enter the first vertical coordinate> "))
Y2 = int(input("please enter the first vertical coordinate> "))

distance = calDistBtwPoints(X, X2, Y, Y2)
print("the distance between the two points is: ", distance)
print("----------------------------------------------------------------------------------------------------------")
