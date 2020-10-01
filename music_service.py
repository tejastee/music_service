from flask import Flask, request, jsonify, send_from_directory, Response
from MusicObj import MusicFile
import constants
from random import randint
import os
from database import MusicData


app = Flask(__name__)
db = MusicData()
music_objects = []


'''

DB Details  -

Database host address:tejastee4.mysql.pythonanywhere-services.com
Username:tejastee4
Password:qazwsx123

CREATE TABLE "Music_data" (
	"File_name"	TEXT,
	"Path"	TEXT NOT NULL,
	PRIMARY KEY("File_name")
);

'''

@app.route('/')
def is_server_on():
    return "OK"


@app.route('/getstream')
def get_stream():
    def generate(path):
        with open(path, "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)

    if music_objects:
        random_int = randint(0, len(music_objects) - 1)
        audio_file = music_objects[random_int]
        return Response(generate(audio_file.path), mimetype="audio/mp3")
    else:
        return jsonify({'error': "Files not init"})


# @app.route('/getallmp3')
# def get_all_mp3():
#     global music_objects
#     music_objects.clear()
#     print("Music Folder is {}".format(MUSIC_DIR))
#     audio_files = os.listdir(MUSIC_DIR)
#     for i in audio_files:
#         if i.endswith(".mp3"):
#             music_objects.append(MusicFile(os.path.join(MUSIC_DIR, i)))
#     audio_list = []
#     if music_objects:
#         for audio in music_objects:
#             audio_list.append(audio.get_as_dict())
#     return jsonify(audio_list)


@app.route('/update_db')
def update_db():
    print("Music Folder is {}".format(constants.MUSIC_DIR))
    audio_files = os.listdir(constants.MUSIC_DIR)
    files = 0
    for i in audio_files:
        if i.endswith(".mp3"):
            print(i, constants.MUSIC_DIR)
            music_obj = MusicFile(os.path.join(constants.MUSIC_DIR, i))
            db.insert_to_music_data(music_obj)
            files += 1
    return jsonify({'Files Inserted' : files})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
