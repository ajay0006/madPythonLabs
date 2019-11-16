import sqlite3
import base64
import time
import webbrowser
import requests
from geolocation.main import GoogleMaps
from lxml import html
import textwrap


def requestUser():
    iD = input("please enter a number from 1 - 24 or press q to exit: ")
    return iD


def testRequests(decrypt):
    address = decrypt
    google_maps = GoogleMaps(api_key="AIzaSyAEk_XVCNBK9RavS6KiXXfQW-fRvMzKt5o")
    location = google_maps.search(location=address)
    print(location.all())


def requestCityCountryFirstNameLastName():
    # City = input('Please enter the name of the city: ')
    # Country = input('Please enter the name of the country: ')
    FName = input('Please enter the student first name: ')
    LName = input('Please enter the student Last name: ')
    return FName, LName


def createConnectionSql(db_file):
    connector = None
    dataCursor = None
    try:
        connector = sqlite3.connect(db_file)
        dataCursor = connector.cursor()
    except sqlite3.Error as e:
        print(e)

    return connector, dataCursor


def getDataViaConnectorFromDb(dataCursor1, dbID):
    dataCursor1.execute("select link from lab10 where id = ?", (dbID,))
    rows = dataCursor1.fetchall()
    for row in rows:
        return row[0]


def decodeRetrievedData(rData):
    test2 = base64.urlsafe_b64decode(rData).decode('utf-8')
    print(test2)
    return test2


def openWebBrowserLink(link):
    webbrowser.open(link, new=2, autoraise=True)


def updateTable(connector, dataCursor2, City, Country, Student, Id):
    dataCursor2.execute("update Lab10 set City=?, Country=?, Student=? where id = ?", (City, Country, Student, Id))
    connector.commit()
    connector.close()


def extractCityCountry(decrypt):
    response = []
    # response = requests.get(decrypt)
    tester = requests.get(decrypt).content.decode('utf-8')
    # testerR = tester.content.decode('utf-8')
    # print(tester)
    testerR = tester.rstrip('\n').split('"')
    # testerR = tester
    for row in testerR:
        response.append(row)
    print('test2', response[35], response[63])
    return response


while True:
    iDValue = requestUser()
    # try:

    if iDValue == 'q':
        exit()

    elif int(iDValue) >= 25:
        print('You have entered a value less than 0 or greater than 24: ')

    elif 24 >= int(iDValue) > 0:
        iDValue2 = int(iDValue)
        connDb, cursor = createConnectionSql('week10Blank.db')
        data = getDataViaConnectorFromDb(cursor, iDValue2)
        decodedValue = decodeRetrievedData(data)
        openWebBrowserLink(decodedValue)
        city, country = extractCityCountry(decodedValue)
        testRequests(decodedValue)
        time.sleep(3)
        FirstName, LastName = requestCityCountryFirstNameLastName()
        updateTable(connDb, cursor, city, country, FirstName, iDValue)

    # except:
    #     print("you have entered an invalid selection")
