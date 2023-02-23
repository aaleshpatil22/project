from flask import Flask
app = Flask(__name__)

@app.route('/post/<int:year>')
def post(year):
    return "Year is %d" %year

@app.route('/version/<float:ver>')
def version(ver):
    return "The version is %0.1f" %ver

if __name__ == '__main__':
    app.run(debug=True)