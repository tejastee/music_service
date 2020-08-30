from flask import Flask,  request, jsonify
from MusicObj import MusicFile
from constants import MUSIC_DIR
import os

app = Flask(__name__)

music_objects = []


@app.route('/')
def is_server_on():
    return "OK"


@app.route('/getallmp3')
def get_all_mp3():
    global music_objects
    audio_files = os.listdir(MUSIC_DIR)
    for i in audio_files:
        music_objects.append(MusicFile(os.path.join(MUSIC_DIR, i)))
    audio_list = []
    if music_objects:
        for audio in music_objects:
            audio_list.append(audio.get_as_dict())
    return jsonify(audio_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
