import csv


# create a function (readDataFileCSV) that opens the file to be worked on
def readDataFileCSV():
    readData = open("2000_BoysNames.txt", "r")
    return readData


def writeInstance(rDFC):
    with open('2000_BoysNames.csv', 'w', newline='\n') as csvReadDatafile:
        csvReadDatafileWriter = csv.writer(csvReadDatafile, quoting=csv.QUOTE_NONNUMERIC)
        csvReadDatafileWriter.writerow(["First Name", "Count"])
        for row in rDFC:
            row_array = row.rstrip("\n").split()
            print(row_array)
            csvReadDatafileWriter.writerow([row_array[0], int(row_array[1])])
        rDFC.close()
        csvReadDatafile.close()


writeInstance(readDataFileCSV())


