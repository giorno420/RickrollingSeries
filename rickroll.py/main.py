from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
