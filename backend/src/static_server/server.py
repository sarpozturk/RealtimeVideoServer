# video_source_server.py

from flask import Flask, render_template

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
    return render_template('video.html')


@app.route('/live')
def live():
    return render_template('live.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
