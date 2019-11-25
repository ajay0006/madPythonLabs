from flask import Flask, render_template, jsonify
from wtforms import Form, StringField, TextField, SelectField
from wtforms.validators import DataRequired
from appModules import createConnectionSql, getTotalNoOfRowsInDb, getAllDataFrmDb
from forms import StudentNameCity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Primaverocatch'

a, b = createConnectionSql()
totalRows = getTotalNoOfRowsInDb(b)
valueLists = getAllDataFrmDb(b, a)


# print(totalRows)
# print('values Test', valueLists)
# print(totalRows)


# @app.route('/')
# def hello_world():
#     return jsonify({'Success': 'Flask API by Damilola'})


@app.route('/')
def index():
    studentName = []
    studentOriginLink = []
    for extract in valueLists:
        # print(extract)
        studentName.append(extract['Student'])
        studentOriginLink.append(extract['Link'])
        # print('name', studentName)
        # print('links', studentOriginLink)
    pairsValues = zip(studentName, studentOriginLink)
    # pairsValuesList = list(pairsValues)
    # print(pairsValuesList)
    # print(pairsValues[0])
    # form = StudentNameCity()
    return render_template('index.html', pairs=pairsValues, the_title='Students & Country Index')


@app.route('/forms')
def forms():
    pass


@app.route('/students')
def students():
    pass


if __name__ == '__main__':
    app.run(debug=True)
