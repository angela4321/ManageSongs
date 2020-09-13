import sqlite3
class Manage:
    def __init__(self):
        self.co = sqlite3.connect("Songs.db")

        self.co.execute('''create table if not exists Songs(
                        ID INT PRIMARY KEY,
                        TITLE TEXT,
                        ARTIST TEXT,
                        GENRE TEXT,
                        NUM_LISTENS TEXT,
                        NUM_LIKES TEXT)''')

    def add_song(self,id,title,genre,artist,num_listens,num_likes):
        self.co.execute("insert into Songs (ID,TITLE,GENRE,ARTIST,NUM_LISTENS,NUM_LIKES)  values(?,?,?,?,?,?)",(id,title,artist,genre,num_listens,num_likes))


    def remove_song(self,id):
        self.co.execute("DELETE from Songs where ID = ?",[id])

    def get_songs(self):
        return self.co.execute("SELECT ID, TITLE, ARTIST, NUM_LISTENS, NUM_LIKES from Songs")

    def close(self):
        self.co.close()

    def letter(self,l):
        s = "select TITLE, ARTIST from Songs where TITLE like '"+l+"%'"
        return self.co.execute(s)

    def get_artist(self,art): #returns all songs from a certain artist
        return self.co.execute("select TITLE, ARTIST, NUM_LISTENS, NUM_LIKES from Songs where Artist = '"+art+"';")

    def get_song_by_likes(self,a,b): #returns songs with num_likes between a and b
        return self.co.execute("select TITLE, ARTIST, NUM_LISTENS, NUM_LIKES from Songs where NUM_LIKES between "+a+" and "+b+";")

    def sort(self,a,b):
        return self.co.execute("select TITLE, ARTIST, NUM_LISTENS, NUM_LIKES from Songs ORDER BY "+b+" "+a+";")