# classical imports for the gfxHat
import csv
import random

from gfxhat import lcd, backlight


def setBacklight():
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    backlight.set_all(r, g, b)
    backlight.show()


# created an empty list that's gonna be used to hold the data from the text file


def generateLists():
    fontFileContent = []
    # created an object instance container for the file i want to open
    with open('font3.txt', newline='', encoding='utf-8-sig') as fontCsvFile:
        # i noticed a slight formatting error, so i formatted the instance to see whitespaces as quotes
        # that way i am able to get each value in a separate index, making it easier to extract the character and its
        # subsequent code
        fontReader = csv.reader(fontCsvFile, delimiter=",", quotechar=',', quoting=csv.QUOTE_MINIMAL)
        # a simple for loop that iterates through the file
        for row in fontReader:
            # i have chosen to use extend rather than extend so i get a single list with a long range of indexes rather
            # than getting a list in a list
            fontFileContent.extend(row)
        # closing of the open instance
        fontCsvFile.close()
        # print(len(fontFileContent), 'length of list')
        #         print statement is just to confirm my output is accurate
        # print(fontFileContent, 'first')
        # fontFileContentCopy = list(fontFileContent)
        return fontFileContent


# this function does one simple thing, it removes the "0x" from the hexadecimal numbers before its passed into the dict
# function, it this way, cos it makes most sense for me and flow of the program is easier to understand
def remove0x(gendList):
    # iterates through the list at index intervals of 2
    for p in range(0, len(gendList), 2):
        # removes the first two characters and appends it to its original list
        gendList[p] = gendList[p][2:]
    return gendList


#  a function that creates a dictionary and maps the odd indexes as keys, and the even indexes as values
def generateDictionary(hexList):
    thisDict = {}
    j = 0
    k = 1
    i = 0
    lengthList = (len(hexList)) / 2
    while i < lengthList:
        thisDict[hexList[k]] = hexList[j]
        j += 2
        k += 2
        i += 1
    return thisDict


# functions take a character argument, traverses the dictionary and returns its key value
def getKeyValue(Char, Dict):
    # creating an empty list
    valueList = []
    # assigning the value key pair to a variable container
    value = Dict.get(Char)
    # loop iterating over the value corresponding to the character key in two's
    for i in range(0, len(value), 2):
        # appending each value pair to the empty list created above, using append cos i want to create multiple lists
        # rather than a single list
        valueList.append(value[i:i + 2])
    # just testing if it works
    # print(valueList, 'wat do i see')
    # you know what this does right lol
    return valueList


# function that converts the value to binary
def keyValueToBinary(keyValue):
    # empty list container
    keyValueListBinary = []
    # testing to see if my code is okay
    # print(len(keyValue))
    # print(type(keyValue))
    # for loop to iterate over the retrieved value from the function above
    for yo in range(0, len(keyValue)):
        # assigning each instance of yo to a list
        yoyo = keyValue[yo]
        # converting the value to a binary, casting it to an int, removing the first 2 characters,and filling it with
        # 8 zeros
        valueBin = bin(int(yoyo, 16))[2:].zfill(8)
        # appending the value to the empty list, prefer append in this case cos i want many list in a list
        keyValueListBinary.append(list(valueBin))
    # regular testing of code
    # print(keyValueListBinary)
    # print(len(keyValueListBinary))

    # another return statement hehe
    return keyValueListBinary


# function that converts the multi list to a 2D array
def convertBinaryListToMultiList(binaryList):
    # iterate tru the list a number of times equivalent to the length of the list, e,g 8 times
    for i in range(len(binaryList)):
        # for each iteration above, iterate n === len(list) times e.g 5 times == 5 * 8 = 40 values
        for j in range(len(binaryList[i])):
            # convert or cast to an int and assign it to the index position
            binaryList[i][j] = int(binaryList[i][j])
    # another test
    # print(binaryList)
    # another return
    return binaryList


# the infamous display object function
def displayObject(obj, x, y):
    i = 0
    for line in obj:
        j = 0
        for pixel in line:
            lcd.set_pixel(x + j, y + i, pixel)
            j = j + 1
        i = i + 1
    lcd.show()


drawChar = str(input("kindly type a character: "))
try:
    A = generateLists()
    B = remove0x(A)
    C = generateDictionary(B)
    D = getKeyValue(drawChar, C)
    E = keyValueToBinary(D)
    F = convertBinaryListToMultiList(E)
    print(F)
    displayObject(F, 63, 31)

except:
    print("you have entered a character whose draw pattern is unavailable at the moment, pls try again later!!!")
