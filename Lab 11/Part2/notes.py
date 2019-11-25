# javascript css and stuff wud be in the static folder
#
# template folder contains all the jinja code and html files and templates

# the app.py will contain all the routes, the webpages would have routes in the route file

@app.route ('/user/<username>')
def user(username):
    return render.template('user.html', username = username,course='cst8279')

# the <abc> is an argument