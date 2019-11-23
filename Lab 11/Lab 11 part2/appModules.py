import sqlite3
import os.path
import base64
import time
import webbrowser
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "week10.db")


# def createConnectionSql(db_file):
#     connector = None
#     dataCursor = None
#     try:
#         connector = sqlite3.connect(db_file)
#         connector.row_factory = sqlite3.Row
#         dataCursor = connector.cursor()
#     except sqlite3.Error as e:
#         print(e)
#
#     return connector, dataCursor

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
    dataCursor2.execute('select * from Lab10')
    data = dataCursor2.fetchall()
    for row in data:
        dataList.append(dict(row))
    connector2.close()
    return dataList


def decodeLink(keyToFind, dictList):
    for eachDict in dictList:
        for key in eachDict.keys():
            if key == keyToFind:
                decodedLink = base64.urlsafe_b64decode(eachDict[key]).decode('utf-8')
                eachDict[key] = decodedLink
    return dictList

# print(os.getcwd())

# def main(db_file):
#     damiObject = Database()
#     a, b = damiObject.createConnectionSql(db_file)
#     totalRows = damiObject.getTotalNoOfRowsInDb(b)
#     value = damiObject.getAllDataFrmDb(b, a)
#     print(value)
#     print(totalRows)
#     return totalRows, value


#
# #
# if __name__ == '__main__':
#     main("week10.db")
#
a, b = createConnectionSql()
totalRows = getTotalNoOfRowsInDb(b)
value = getAllDataFrmDb(b, a)
print(type(value))
print(value)
test = decodeLink('Link', value)
print(test)
