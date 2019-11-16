import sqlite3
import base64
import time
import webbrowser


# input statement to request the id
def requestUser():
    iD = input("please enter a number from 1 - 24 or press q to exit: ")
    return iD


# creates a connection to the database as well as an edit instance, and returns the open instance
def createConnectionSql(db_file):
    connector = None
    dataCursor = None
    try:
        connector = sqlite3.connect(db_file)
        dataCursor = connector.cursor()
    except sqlite3.Error as e:
        print(e)

    return connector, dataCursor


# gets the total number of rows so i can use it for my if else statement
def getTotalNoOfRowsInDb(dataCursor1):
    noOfRows = dataCursor1.execute("select count(*) from lab10")
    return noOfRows


# takes edit instance and id inputed by user as variables, to select data from database
# returns the fetched data from the database
def getDataViaConnectorFromDb(dataCursor2, dbID):
    dataCursor2.execute("select link from lab10 where id = ?", (dbID,))
    rows = dataCursor2.fetchall()
    for row in rows:
        return row[0]


# decodes the fetched data, returns the decoded data
def decodeRetrievedData(rData):
    test2 = base64.urlsafe_b64decode(rData).decode('utf-8')
    print(test2)
    return test2


# opens the weblink in the default browser
def openWebBrowserLink(link):
    webbrowser.open(link, new=2, autoraise=True)


# input statement to get the city, country, first name and return these values
def requestCityCountryFirstNameLastName():
    City = str(input('Please enter the name of the city: '))
    Country = str(input('Please enter the name of the country: '))
    FName = str(input('Please enter the student first name: '))
    return City, Country, FName


# updates the database using the connection instance, and closes the connection when done
def updateTable(connector, dataCursor2, City, Country, Student, Id):
    dataCursor2.execute("update Lab10 set City=?, Country=?, Student=? where id = ?", (City, Country, Student, Id))
    connector.commit()
    connector.close()


# simple while loop that keeps running until 'q' is pressed
x = 0
while x == 0:
    iDValue = requestUser()
    try:

        if iDValue == 'q':
            exit()

        elif 0 >= int(iDValue) >= 25:
            print('You have entered a value less than 0 or greater than 24: ')

        elif 24 >= int(iDValue) > 0:
            iDValue2 = int(iDValue)
            connDb, cursor = createConnectionSql('week10.db')
            noOfRows, data = getDataViaConnectorFromDb(cursor, iDValue2)
            decodedValue = decodeRetrievedData(data)
            openWebBrowserLink(decodedValue)
            # extractCityCountry(decodedValue)
            time.sleep(3)
            city, country, FirstName = requestCityCountryFirstNameLastName()
            updateTable(connDb, cursor, city, country, FirstName, iDValue)

    except:
        print("you have entered an invalid selection")
        x += 1
