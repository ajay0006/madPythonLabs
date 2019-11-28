# javascript css and stuff wud be in the static folder
#
# template folder contains all the jinja code and html files and templates

# the app.py will contain all the routes, the webpages would have routes in the route file

@app.route ('/user/<username>')
def user(username):
    return render.template('user.html', username = username,course='cst8279')

# the <abc> is an argument

# create a u
# notes on if statements

flask notes
# {% if index %}active{% endif %}

# this gets the value from a field if we arent using forms
request.args.get(<field_name>)
requesr.args[<field_names>]

# this gets the value if we are using forms
request.form.get(<field_name>)
requesr.form[<field_names>]

