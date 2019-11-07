import csv


# create a function (readDataFileCSV) that opens both the files to be worked on
def readBoys_GirlDataFileCSV():
    # this opens the two files and holds it in the variables readBoyData and readGirlData
    readBoyData = open("2000_BoysNames.txt", "r")
    readGirlData = open("2000_GirlsNames.txt", "r")
    # returns the readData variable
    return readBoyData, readGirlData


# created a function that will take the text file as an argument and print the contents to a csv file
def writeInstance(rDFC, fileName):
    # opens the csv file if it exists, if not it creates it, with write only permissions and appends a new line after
    # write sequence
    with open(fileName, 'w', newline='\n') as csvReadDatafile:
        # "AAA" dialect is set, and a variable holds the instance of how data would be written into the csv file
        # i have chosen to have the numeric numbers non quoted so as to adhere to the assignment rules
        csvReadDatafileWriter = csv.writer(csvReadDatafile, quoting=csv.QUOTE_NONNUMERIC)
        # this prints the header and quotes both
        csvReadDatafileWriter.writerow(["First Name", "Count"])
        # iterates through the text data file
        for row in rDFC:
            # this strips the data of indents and separates it by spaces
            row_array = row.rstrip("\n").split()
            # this is to test that my output is as i desire, only cosmetic line of code
            print(row_array)
            # this writes the data based on the parameters set in the dialect in the comment "AAA" above
            # this ensures that the numbers aren't quoted as required by the assignment rules
            csvReadDatafileWriter.writerow([row_array[0], int(row_array[1])])
        # closes the text file
        rDFC.close()
        # close the write instance
        csvReadDatafile.close()


# function that gives the option for you  to choose what you want to name the output csv file for the boys data
def getNameBoysOfFile():
    boysFileName = str(input('please enter what you would like to name the boys file with the csv extension'))
    return boysFileName


# function that gives the option for you  to choose what you want to name the output csv file for the girls data
def getNameOfGirlsFile():
    girlsFileName = str(input('please enter what you would like to name the girls file with the csv extension'))
    return girlsFileName


# stores the the boys data retrieved from the function
boys = readBoys_GirlDataFileCSV()[0]

# stores the the girls data retrieved from the function
girls = readBoys_GirlDataFileCSV()[1]

# passes the boys data, as well a the file name chosen
writeInstance(boys, getNameBoysOfFile())
# passes the girls data, as well a the file name chosen
writeInstance(girls, getNameOfGirlsFile())
