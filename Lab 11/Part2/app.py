import re
import webbrowser
import json
from flask import Flask, render_template, request
from appModules import main

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Primaverocatch'

valueLists = main()[1]
totalNoOfRows = main()[0]


@app.route('/')
# @app.route('/index')
def index():
    studentName = []
    studentOriginLink = []
    for extract in valueLists:
        studentName.append(extract['Student'])
        studentOriginLink.append(extract['Link'])
    pairsValues = zip(studentName, studentOriginLink)
    return render_template('index.html', pairs=pairsValues, the_title='Students & Country Index')


@app.route('/displayAll.html', methods=['POST', 'GET'])
def displayAll():
    if request.method == 'GET':
        studentName = []
        studentCity = []
        studentCountry = []
        studentOriginLink = []
        headers = ['Student Name', 'City', 'Country']
        for extract in valueLists:
            studentName.append(extract['Student'])
            studentCity.append(extract['City'])
            studentCountry.append(extract['Country'])
            studentOriginLink.append(extract['Link'])
        fourPairsValues = zip(studentName, studentCity, studentCountry, studentOriginLink)
        return render_template('displayAll.html', fourPairs=fourPairsValues, headers=headers,
                               the_title='Full Student and Origin Table')


@app.route('/testMap.html')
def testMap():
    links = []
    combo = []
    for dicts in valueLists:
        for key in dicts.keys():
            if key == 'Link':
                links.append(dicts[key])
    temp = re.search('@([0-9]?[0-9]\.[0-9]*),([0-9]?[0-9]\.[0-9]*)', links[0], re.DOTALL)
    latitude = temp.groups()[0]
    longitude = temp.groups()[1]
    combo.append(float(longitude))
    combo.append(float(latitude))
    print(combo)
    # return render_template('testMap.html', latLong=map(json.dumps, combo), the_title='Fly to a location')
    return render_template('testMap.html', latLong=json.dumps(combo), the_title='Fly to a location')


@app.route('/index/<Link>')
def openWeb(Link):
    webbrowser.open(Link, new=2, autoraise=True)


if __name__ == '__main__':
    app.run(debug=True)
