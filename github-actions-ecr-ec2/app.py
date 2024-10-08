from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from my CI/CD powered Flask app! V2 '

if __name__ == '__main__':
    print(f"__name__ is {__name__}")
    app.run(debug=True, host='0.0.0.0',port=5001)
