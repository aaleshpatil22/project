from flask import Flask,redirect,url_for,request
app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome(name):
    return "Welcome %s" %name

@app.route('/failure')
def failure():
    return "Not valid request"

@app.route('/login',methods=['POST',"GET"])
def login():
    if request.method == 'POST':
        uname = request.form['uname']
        return redirect(url_for('welcome',name=uname))
    else:
        return redirect(url_for('failure'))

if __name__ == "__main__":
    app.run(debug=True)