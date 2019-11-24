from flask import Flask, render_template, jsonify
from appModules import createConnectionSql, getTotalNoOfRowsInDb, getAllDataFrmDb

app = Flask(__name__)

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
    pairsValuesList = list(pairsValues)
    # print(pairsValuesList)
    # print(pairsValues[0])
    return render_template('index.html', pairs=pairsValuesList, the_title='Students & Country Index')


if __name__ == '__main__':
    app.run(debug=True)
