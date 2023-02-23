from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return (" NLP-Based Fake Reviews Detection")

if __name__ == '__main__':
    app.run(debug=True)
