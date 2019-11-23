import sqlite3
import base64
import time
import webbrowser


def createConnectionSql(db_file):
    connector = None
    dataCursor = None
    try:
        connector = sqlite3.connect(db_file)
        dataCursor = connector.cursor()
    except sqlite3.Error as e:
        print(e)

    return connector, dataCursor


def getTotalNoOfRowsInDb(dataCursor1):
    dataCursor1.execute("select count(*) from lab 10")
    noOfRows = dataCursor1.fetchall()
    return int(noOfRows[0][0])


def getAllDataFrmDb(dataCursor2, connector2):
    dataList = []
    dataCursor2.execute('select * from lab10')
    data = dataCursor2.fetchall()
    for row in data:
        dataList.extend(row)
    connector2.close()
    return dataList
