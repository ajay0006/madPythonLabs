import sqlite3
import base64
import webbrowser
import os.path
from sqlite3.dbapi2 import Connection, Cursor
from typing import Union


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, "week10.db")


class Database:
    dataCursor: Cursor
    connector: Connection
    db_path: Union[bytes, str]
    BASE_DIR: Union[bytes, str]

    # this is to ensure there arent any path errors when accessing the database file
    def osPath(self, db_file):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.BASE_DIR, db_file)

    # connection to the database is created, row_factory gets the data as a dictionary
    def createConnectionSql(self):
        self.connector = None
        self.dataCursor = None
        try:
            self.connector = sqlite3.connect(self.db_path)
            self.connector.row_factory = sqlite3.Row
            self.dataCursor = self.connector.cursor()
        except sqlite3.Error as e:
            print(e)

    # get the total number of rows returned
    def getTotalNoOfRowsInDb(self):
        self.dataCursor.execute("select count(*) from lab10")
        noOfRows = self.dataCursor.fetchall()
        return int(noOfRows[0][0])

    # gets all the data from the database as a dictionary and also decodes the links
    def getAllDataFrmDb(self):
        dataList = []
        keyToFind = "Link"
        self.dataCursor.execute('select * from Lab10')
        data = self.dataCursor.fetchall()
        for row in data:
            dataList.append(dict(row))
        for eachDict in dataList:
            for key in eachDict.keys():
                if key == keyToFind:
                    decodedLink = base64.urlsafe_b64decode(eachDict[key]).decode('utf-8')
                    eachDict[key] = decodedLink
        self.connector.close()
        return dataList

    @staticmethod
    def openWebBrowserLink(Link):
        webbrowser.open(Link, new=1, autoraise=True)


def main():
    dami = Database()
    dami.osPath('week10.db')
    dami.createConnectionSql()
    totalRows = dami.getTotalNoOfRowsInDb()
    value = dami.getAllDataFrmDb()
    return totalRows, value


if __name__ == '__main__':
    main()

# a, b = createConnectionSql()
# totalRows = getTotalNoOfRowsInDb(b)
# value = getAllDataFrmDb(b, a)
# print(type(value))
# print(value)

# doesZipWork(value)
