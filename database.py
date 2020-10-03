import mysql.connector
import logging
import constants
from MusicObj import MusicFile

'''
 CREATE USER 'root' IDENTIFIED BY 'password';

sudo mysqladmin -u root password wqsa@12

CREATE TABLE `tejastee4$music_service`.`music_data` (
  `title` VARCHAR(45) NOT NULL,
  `artist_name` VARCHAR(45) NULL,
  `album` VARCHAR(45) NULL,
  `genre` VARCHAR(45) NULL,
  `length` DECIMAL(5) NULL,
  PRIMARY KEY (`title`));

'''

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:  %(message)s', handlers=[logging.StreamHandler()])


def sample():
    logging.debug("Connecting . . ")
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='wqsa@12',
        database='testdb'
    )
    logging.debug("Connected!")

    mycursor = mydb.cursor()
    mycursor.execute('show TABLES;')
    print(mycursor.fetchall())

    sql = "INSERT INTO music_data (title, artist_name, album, genre, length) VALUES (%s, %s, %s, %s, %s)"
    val = ("John", "Highway 21", "That", "Rock", "123.35")

    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


class MySqlDatabase:
    def __init__(self):
        self.mydb = None
        self.cursor = None
        self.connect()

    def connect(self):
        logging.debug("Connecting......")
        self.mydb = mysql.connector.connect(
            **constants.DB_CRED
        )
        self.cursor = self.mydb.cursor()
        logging.debug("Connect Succesful!")

    def commit(self):
        logging.debug("Commit DB!")
        self.mydb.commit()

    def check_conn(self):
        if self.mydb and self.mydb.is_connected():
            return True
        else:
            self.connect()
            return True


class MusicData(MySqlDatabase):
    def __init__(self):
        MySqlDatabase.__init__(self)
        logging.debug("Music Data!")

    def _check_connection(func):
        def _wrapper(self, *args, **kwargs):
            if self.check_conn():
                return func(self, *args, **kwargs)
        return _wrapper

    @_check_connection
    def get_all(self):
        self.cursor.execute(
            "select title, artist_name, album, genre, CAST(length AS CHAR) length, path from music_data")
        myresult = self.cursor.fetchall()
        logging.debug(myresult)
        return myresult

    @_check_connection
    def insert_to_music_data(self, music_object):
        logging.debug("Inserting - {}".format(music_object))
        sql = "INSERT IGNORE INTO music_data (title, artist_name, album, genre, length, path) VALUES (%s, %s, %s, %s, %s, %s)"
        values = [music_object.title, music_object.artist_name, music_object.album, music_object.genre,
                  music_object.length, music_object.path]
        self.cursor.execute(sql, values)
        self.commit()
        print(self.cursor.rowcount, "record inserted.")


if __name__ == '__main__':
    db = MusicData()
    print(db)
    db.get_all()
