from flask import Flask

app = Flask(__name__)

@app.route('/')
def is_alive():
    return f'Yes, the app is alive.'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)

