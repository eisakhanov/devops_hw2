#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello CI-CD</title>
    </head>
    <body>
        <h1>Hello, CI-CD!</h1>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
