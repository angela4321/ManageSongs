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
        return self.co.execute("SELECT ID, TITLE, ARTIST, GENRE,NUM_LISTENS, NUM_LIKES from Songs")

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

    def filter(self,artist,genre,min_listens,max_listens,min_likes,max_likes,sort_by, order):
        s = "select ID, TITLE, ARTIST, GENRE, NUM_LISTENS, NUM_LIKES from Songs where "
        if artist!=None:
            s+= "ARTIST = '"+artist+"' "
        if genre!=None:
            if artist!=None:
                s+="AND "
            s+= "GENRE = '"+genre+"' "
        if artist!=None or genre!=None:
            s+="AND "
        s+="NUM_LISTENS between "+str(min_listens)+" and "+str(max_listens)+" AND NUM_LIKES between "+str(min_likes)+" and "+str(max_likes)+" ORDER BY "+sort_by+" "+order+";"

        return self.co.execute(s)