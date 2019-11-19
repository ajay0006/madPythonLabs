from flask import Flask, render_template
from modules import convert_to_dict as conv

app = Flask(__name__)

presidents_List = conv("presidents.csv")
print(presidents_List)


@app.route('/')
def index():
    heading = '<h1>Welcome to The Presidential Flask Example!</h1>'
    test1 = '<p>' + presidents_List[0]['President']
    test2 = ", born in " + presidents_List[0]['Birthplace'] + '.<p>'
    return heading + test1 + test2
    # return '<h1>Welcome to the presidential Flask example!</h1>'


# your code here


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
