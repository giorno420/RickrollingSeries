import os
from flask import Flask, Response

app = Flask(__name__)


def responseredirect():
    response = Response()
    response.headers['Refresh'] = "5; url=https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"
    return response

@app.route('/')
def index():
    return responseredirect()


@app.errorhandler(404)
def notfound(e):
    return responseredirect()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
