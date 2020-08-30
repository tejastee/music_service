import eyed3


class MusicFile:
    def __init__(self, path):
        self.path = path
        self.audio_file = eyed3.load(path)
        self.title = self.audio_file.tag.title
        self.artist_name = self.audio_file.tag.artist
        self.album = self.audio_file.tag.album
        self.genre = self.audio_file.tag.genre
        self.length = self.audio_file.info.time_secs
        print(self.audio_file.info)

    def get_as_dict(self):
        dict = {}
        dict["title"] = self.title
        dict["artist_name"] = self.artist_name
        dict["album"] = self.album
        dict["genre"] = self.genre
        dict["length"] = self.length
        return dict

    def __str__(self):
        return "{}-{}-{}-{}-{}".format(self.title, self.artist_name, self.album, self.length, self.genre)


if __name__ == '__main__':
    print(MusicFile('./music/By Myself.mp3'))