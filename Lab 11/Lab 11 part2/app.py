from flask import Flask, render_template
from appModules import createConnectionSql, getTotalNoOfRowsInDb, getAllDataFrmDb

a, b = createConnectionSql()
totalRows = getTotalNoOfRowsInDb(b)
value = getAllDataFrmDb(b, a)
# print(totalRows)
print(value)
print(totalRows)
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
