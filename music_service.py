from flask import Flask,  request, jsonify
from MusicObj import MusicFile
import os

app = Flask(__name__)
MUSIC_DIR = "./music"

music_objects = []

@app.route('/')
def is_server_on():
    return "OK"


@app.route('/getallmp3')
def get_all_mp3():
    global music_objects
    audio_files = os.listdir(MUSIC_DIR)
    for i in audio_files:
        print(i)
        music_objects.append(MusicFile(i))



@app.route('/info')
def info():
    a = {
     "asdasd":123
    }
    return jsonify(a)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

