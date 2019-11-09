import csv


# this function gets the filename from the user, casts it into a string, stores it in a variable and returns the
# variable
def getFileName():
    fileName = str(input("Please Enter your File name with extension: "))
    return fileName


# this function creates an empty list, opens a read instance, and writes the content to the empty list
# the encoding ensure there are no errors with the encoding conversion
def openFile(fileName):
    listItems = []
    with open(fileName, 'r', newline='\n', encoding='utf-8-sig') as csvFile:
        # testReader = csv.reader(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        testReader = csv.reader(csvFile)
        for row in testReader:
            listItems.append(row)
        return listItems


A = getFileName()
print(openFile(A))
