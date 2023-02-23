from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return render_template('submit.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)