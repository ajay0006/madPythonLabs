from flask import Flask, render_template
from modules import convert_to_dict as conv

app = Flask(__name__)

presidents_List = conv("presidents.csv")
print(presidents_List)


@app.route('/')
def index():
    # heading = '<h1>Welcome to The Presidential Flask Example!</h1>'
    # test1 = '<p>' + presidents_List[0]['President']
    # test2 = ", born in " + presidents_List[0]['Birthplace'] + '.<p>'
    president_Ids = []
    presidentNames = []
    for presido in presidents_List:
        president_Ids.append(presido['Presidency'])
        presidentNames.append(presido['President'])
    pairs_list = zip(president_Ids, presidentNames)
    return render_template('index.html', pairs=pairs_list, the_title="Presidents Index")
    # return heading + test1 + test2
    # return '<h1>Welcome to the presidential Flask example!</h1>'


@app.route('/president/<num>')
def detail(num):
    for president in presidents_List:
        if president['Presidency'] == num:
            pres_dict = president
            break
    return render_template('president.html', pres=pres_dict, the_title=pres_dict['President'])


# test = index()
# print(test[2])

# your code here


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
