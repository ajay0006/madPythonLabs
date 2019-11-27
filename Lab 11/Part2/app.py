from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
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

# venv/Lib/site-packages/flask_bootstrap/static/css/bootstrap.min.css
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


@app.route('/displayAll.html')
def displayAll():
    studentName = []
    studentCity = []
    studentCountry = []
    studentOriginLink = []
    for extract in valueLists:
        studentName.append(extract['Student'])
        studentCity.append(extract['City'])
        studentCountry.append(extract['Country'])
        studentOriginLink.append(extract['Link'])
    fourPairsValues = zip(studentName, studentCity, studentCountry, studentOriginLink)
    test = list(fourPairsValues)
    return render_template('displayAll.html', fourPairs=test,
                           the_title='Full Student and Origin Table')


if __name__ == '__main__':
    app.run(debug=True)
