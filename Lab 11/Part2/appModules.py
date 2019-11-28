import sqlite3
import os.path
import base64
import time
import webbrowser
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "week10.db")


def createConnectionSql():
    connector = None
    dataCursor = None
    try:
        with sqlite3.connect(db_path) as db:
            connector = db
            connector.row_factory = sqlite3.Row
            dataCursor = connector.cursor()
    except sqlite3.Error as e:
        print(e)
    return connector, dataCursor


def getTotalNoOfRowsInDb(dataCursor1):
    dataCursor1.execute("select count(*) from lab10")
    noOfRows = dataCursor1.fetchall()
    return int(noOfRows[0][0])


def getAllDataFrmDb(dataCursor2, connector2):
    dataList = []
    keyToFind = "Link"
    dataCursor2.execute('select * from Lab10')
    data = dataCursor2.fetchall()
    for row in data:
        dataList.append(dict(row))
    for eachDict in dataList:
        for key in eachDict.keys():
            if key == keyToFind:
                decodedLink = base64.urlsafe_b64decode(eachDict[key]).decode('utf-8')
                eachDict[key] = decodedLink
    connector2.close()
    return dataList


def openWebBrowserLink(Link):
    webbrowser.open(Link, new=1, autoraise=True)


def doesZipWork(bigList):
    studentName = []
    origin = []
    for extract in bigList:
        studentName.append(extract['Student'])
        origin.append(extract['Link'])
    combo = zip(studentName, origin)
    # print(list(combo))
    comboList = list(combo)
    # print(comboList[0][0],comboList[0][1])
    # print(set(combo)[0][1])
    # print(combo[0][0])


# a, b = createConnectionSql()
# totalRows = getTotalNoOfRowsInDb(b)
# value = getAllDataFrmDb(b, a)
# print(type(value))
# print(value)

# doesZipWork(value)
