import csv

# created an empty list that's gonna be used to hold the data from the text file
fontFileContent = []


def generateLists():
    # created an object instance container for the file i want to open
    with open('font3.txt', newline='') as fontCsvFile:
        # i noticed a slight formatting error, so i formatted the instance to see whitespaces as quotes
        # that way i am able to get each value in a separate index, making it easier to extract the character and its
        # subsequent code
        fontReader = csv.reader(fontCsvFile, delimiter=",", quotechar=',', quoting=csv.QUOTE_MINIMAL)
        # a simple for loop that iterates through the file
        for row in fontReader:
            # i have chosen to use extend rather than extend so i get a single list with a long range of indexes rather
            # than getting a list in a list
            fontFileContent.extend(row)
        #         print statement is just to confirm my output is accurate
        fontCsvFile.close()
        print(len(fontFileContent), 'length of list')
        return fontFileContent
    # print(fontFileContent)


def generateDictionary(hexList):
    thisDict = {}
    j = 0
    k = 1
    i = 0
    lengthList = (len(fontFileContent))/2
    while i < lengthList:
        thisDict[hexList[k]] = hexList[j]
        j += 2
        k += 2
        i += 1
    return thisDict


b = generateLists()
print(generateDictionary(b))

# dami your gonna have to google how to convert a list to a dictionary, should be easy
# that's all that is left to do
