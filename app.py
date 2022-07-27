from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/name')
def Name():
    return "Welcome Reshma!"    

if __name__ == "__main__":
    app.run(debug=True)
