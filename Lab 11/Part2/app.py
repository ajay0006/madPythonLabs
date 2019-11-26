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
print(valueLists)


# print(totalRows)
# print('values Test', valueLists)
# print(totalRows)


# @app.route('/')
# def hello_world():
#     return jsonify({'Success': 'Flask API by Damilola'})


@app.route('/')
@app.route('/index')
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


@app.route('/students')
def students():
    return render_template('search-students.html')


@app.route('/forms')
def forms():
    return render_template('displayAll.html')


@app.route('/displayAll.html')
def displayAll():
    studentName = []
    studentCity = []
    studentCountry = []
    for extract in valueLists:
        studentName.append(extract['Student'])
        studentCity.append(extract['City'])
        studentCountry.append(extract['Country'])
        triplePairsValues = zip(studentName,studentCity,studentCountry)
        return render_template('displayAll.html', triplePairs = triplePairsValues, the_title='Full Student and Origin Table')



if __name__ == '__main__':
    app.run(debug=True)
