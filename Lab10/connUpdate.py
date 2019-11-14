import sqlite3
import base64
import webbrowser
from geolocation.main import GoogleMaps
import requests
from lxml import html
import textwrap


# import geolocation
# from geolocation.main import GoogleMaps


def request():
    try:
        userRequest = int(input("Please enter a number from 1 - 24: "))
        if userRequest == 'q':
            exit()
        elif 24 <= userRequest < 0:
            print('You have entered a value less than 0 or greater than 24')
        elif 24 >= userRequest > 0:
            return userRequest

    except:
        print("you have entered an invalid selection")


def createConnectionSql(db_file):
    connector = sqlite3.connect(db_file)
    return connector


def getDataViaConnectorFromDb(connection):
    dataCursor = connection.cursor()
    dataCursor.execute("select link from lab10 where id = ?", (request(),))
    rows = dataCursor.fetchall()
    for row in rows:
        return row[0]


def decodeRetrievedData(data):
    test2 = base64.urlsafe_b64decode(data).decode('utf-8')
    print(test2)
    return test2


def openWebBrowserLink(link):
    webbrowser.open(link, new=2, autoraise=True)


sqlConn = createConnectionSql('week10 - Test.db')
selectQuery = getDataViaConnectorFromDb(sqlConn)
decrypt = decodeRetrievedData(selectQuery)
openWebBrowserLink(decrypt)


# def requestsTest():
#     term = 'meta content'
#     resp = requests.get(decrypt + term)
#     # print('begin' + resp.text)
#     root = html.fromstring(resp.text)
#     print('begin', root, '2')
# #
#     for sel in root:
#         print(sel)
# #         if sel.text:
# #             s = sel.text.strip()
# #             print(s)
# #             if len(s) > 3:
# #                 print(textwrap.fill(s, width=50))
#
#     # print(resp.text)


def updateCityCountry():
    response = []
    # response = requests.get(decrypt)
    tester = requests.get(decrypt).content.decode('utf-8')
    # testerR = tester.content.decode('utf-8')
    # print(tester)
    testerR = tester.rstrip('\n').split('"')
    # testerR = tester
    for row in testerR:
        response.append(row)
    print('test2', response[35])


#
# def testRequests():
#     address = decrypt
#     google_maps = GoogleMaps(api_key="AIzaSyAEk_XVCNBK9RavS6KiXXfQW-fRvMzKt5o")
#     location = google_maps.search(location=address)
#     print(location.all())
#
#
# testRequests()
# requestsTest()
updateCityCountry()
