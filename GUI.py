from tkinter import *
from Manage import Manage

m = Manage()
root = Tk()

add_song = LabelFrame(root,padx=5,pady=5)
add_song.grid(row=0,column=0)

#add components allowing users to add a song
label1 = Label(add_song,text="Title")
label1.grid(row=0,column=0)
entry1 = Entry(add_song,width=20)
entry1.grid(row=1,column=0)

label2 = Label(add_song,text="Artist")
label2.grid(row=0,column=1)
entry2 = Entry(add_song,width=20)
entry2.grid(row=1,column=1)

label3 = Label(add_song,text="Genre")
label3.grid(row=0,column=2)
entry3 = Entry(add_song,width=20)
entry3.grid(row=1,column=2)

label4 = Label(add_song,text="Listens")
label4.grid(row=0,column=3)
entry4 = Entry(add_song,width=20)
entry4.grid(row=1,column=3)

label5 = Label(add_song,text="Likes")
label5.grid(row=0,column=4)
entry5 = Entry(add_song,width=20)
entry5.grid(row=1,column=4)

#add components allowing users to filter for songs
filter = LabelFrame(root)
filter.grid(row=2,column=0)



#filter by Artist
artist_label = Label(filter,text="Artist")
artist_label.grid(row=0,column=0)
artist_entry = Entry(filter)
artist_entry.grid(row=1,column=0)

#filter by Genre
genre_label = Label(filter,text="Genre")
genre_label.grid(row=0,column=1)
genre_entry = Entry(filter)
genre_entry.grid(row=1,column=1)



#filter by min and max listens
min_listen_label = Label(filter,text="Min listens")
min_listen_label.grid(row=0,column=2)
min_listen_entry = Entry(filter,width=10)
min_listen_entry.grid(row=1,column=2)

max_listen_label = Label(filter,text="Max listens")
max_listen_label.grid(row=0,column=3)
max_listen_entry = Entry(filter,width=10)
max_listen_entry.grid(row=1,column=3)

#filter by min and max likes
min_like_label = Label(filter,text="Min likes")
min_like_label.grid(row=0,column=4)
min_like_entry = Entry(filter,width=10)
min_like_entry.grid(row=1,column=4)

max_like_label = Label(filter,text="Max likes")
max_like_label.grid(row=0,column=5)
max_like_entry = Entry(filter,width=10)
max_like_entry.grid(row=1,column=5)

#different sorting options
sort_label = Label(filter,text="Sort by")
sort_label.grid(row=0,column=6)
sort = OptionMenu(filter,None,"Alphabetical","Most listened to","Least listened to","Most liked","Least liked")
sort.grid(row=1,column=6)

filter_button = Button(filter,text="Filter")
filter_button.grid(row=2,column=0,columnspan=6)

list = []
songs = LabelFrame(root)
songs.grid(row=1,column=0)
id = 0
def submit():
    global id
    id+=1
    title = entry1.get()
    artist = entry2.get()
    genre = entry3.get()
    listens = entry4.get()
    likes = entry5.get()

    entry1.delete(0,'end')
    entry2.delete(0,'end')
    entry3.delete(0,'end')
    entry4.delete(0,'end')
    entry5.delete(0,'end')
    m.add_song(id,title,artist,genre,listens,likes)
    temp = m.get_songs()
    i = 2
    for row in temp:
        i+=1
        s = "Song iD: "+ str(row[0])+"  Title: "+str(row[1])+" "+"  Artist: "+str(row[2])+"  Genre: "+str(row[3])+"  Listens: "+str(row[4])+"  Likes: "+str(row[5])
        lab = Label(songs,text=s)
        lab.grid(row=i,column=0,columnspan=5)

submit = Button(add_song,text="Submit", command = submit)
submit.grid(row=2,column=2)
root.mainloop()