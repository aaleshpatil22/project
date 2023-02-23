from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/user')
def show_user():
    return "Hello admin user"

@app.route('/guest/<guest>')
def show_guest(guest):
    return "Hello %s" %guest

@app.route('/user/<name>')
def admin(name):
    if name == "aalesh":
        return redirect(url_for('show_user'))
    else:
        return redirect(url_for('show_guest',guest=name))

if __name__ == '__main__':
    app.run(debug=True)
