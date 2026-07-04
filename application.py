from flask import render_template, Flask
application = Flask(__name__)



@application.route('/help')
def helppage():
    return "<b><font color=blue>this is help page!!!!!!!!!!!!</font></b>"

@application.route('/user')
def userpage():
    return "User"

@application.route('/user/<name>')
def username(name):
    return "Hello " + name.upper()

@application.route('/path/<path:subpath>')
def print_subpath(subpath):
    return "Subpath is: " + subpath

@application.route('/kvadrat/<int:x>')
def calc(x):
    return "Kvadrat ot: " + str(x) + ' = ' + str(x * x)

@application.route('/')
def html_page():
    return render_template('mypage.html')



#---------Main--------------------
if __name__ == '__main__':
    application.debug = True
    application.run()
#---------------------------------
