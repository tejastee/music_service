import eyed3
eyed3.log.setLevel("ERROR")


class MusicFile:
    def __init__(self, path):
        self.path = path
        self.audio_file = eyed3.load(path)
        self.title = self.audio_file.tag.title
        self.artist_name = self.audio_file.tag.artist
        self.album = self.audio_file.tag.album
        self.genre = str(self.audio_file.tag.genre)
        self.length = self.audio_file.info.time_secs

    def get_as_dict(self):
        dict_obj = {}
        dict_obj["title"] = self.title
        dict_obj["artist_name"] = self.artist_name
        dict_obj["album"] = self.album
        dict_obj["genre"] = str(self.genre)
        dict_obj["length"] = self.length
        return dict_obj

    def __str__(self):
        return "{}-{}-{}-{}-{}".format(self.title, self.artist_name, self.album, self.length, self.genre)


if __name__ == '__main__':
    print(MusicFile('static/By Myself.mp3'))