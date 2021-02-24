from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World ! - Pyflask Demo'

@app.route('/version')
def get_version():
    return 'App version : <b>2.0</b>'

@app.route('/test')
def get_test():
    return 'You are accessing /test endpoint'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
