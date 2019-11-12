import sqlite3
import base64


def request():
    try:
        userRequest = int(input("Please enter a number from 1 - 24: "))
        if 24 <= userRequest < 0:
            print('You have entered a value less than 0 or greater than 24')
        if 24 >= userRequest > 0:
            return userRequest

    except:
        print("you have entered an invalid selection")


def createConnectionSql():

print(request())
