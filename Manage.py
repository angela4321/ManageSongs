import sqlite3
class Manage:
    def __init__(self):
        self.co = sqlite3.connect("Songs.db")

        self.co.execute('''create table if not exists Songs(
                        ID INT,
                        TITLE TEXT,
                        ARTIST TEXT,
                        NUM_LISTENS TEXT,
                        NUM_LIKES TEXT)''')

    def add_song(self,id,title,artist,num_listens,num_likes):
        self.co.execute("insert into Songs (ID,TITLE,ARTIST,NUM_LISTENS,NUM_LIKES)  values(?,?,?,?,?)",(id,title,artist,num_listens,num_likes))


    def remove_song(self):
        print("here")

    def get_song(self):
        print("here")