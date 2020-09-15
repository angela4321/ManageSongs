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
filter.grid(row=3,column=0)

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
v = StringVar(root)
v.set("iD")
sort_by = "iD"
order = "ASC"
def sort_filter(value):
    global sort_by
    global order
    if value=="Alphabetical":
        sort_by = "TITLE"
        order = "ASC"
    elif value == "Most listened to":
        sort_by = "NUM_LISTENS"
        order = "DESC"
    elif value == "Least listened to":
        sort_by = "NUM_LISTENS"
        order = "ASC"
    elif value == "Most liked":
        sort_by = "NUM_LIKES"
        order = "DESC"
    elif value == "Least liked":
        sort_by = "NUM_LIKES"
        order = "ASC"


#Add drop down menu for sorting
sort_label = Label(filter,text="Sort by")
sort_label.grid(row=0,column=6)
ops = ["iD","Alphabetical","Most listened to","Least listened to","Most liked","Least liked"]
sort = OptionMenu(filter,v,*ops,command = sort_filter)
sort.grid(row=1,column=6)


#add songs and display
list = []
ids = []
songs = LabelFrame(root)
songs.grid(row=2,column=0)
id = 0
def submit():
    global id
    global list
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

    s = "Song iD: " + str(id) + "  Title: " + str(title) + " " + "  Artist: " + str(artist) + "  Genre: " + str(
        genre) + "  Listens: " + str(listens) + "  Likes: " + str(likes)
    lab = Label(songs, text=s)
    list.append(lab)
    ids.append(id)

    for i in list:
       i.pack_forget()
    i = 2
    for j in range(len(list)):
        if j >= len(list)-5:
            list[j].grid(row=i,column=0)
            i+=1


#allow user to remove song
remove_frame = LabelFrame(root)
remove_frame.grid(row=1,column=0)

remove_label = Label(remove_frame,text = "Enter the iD of the song you want to remove")
remove_label.grid(row=0,column=0)

remove_entry = Entry(remove_frame,width=10)
remove_entry.grid(row=1,column=0)

def rem():

    for i in list:
       i.pack_forget()
    try:
        element = int(remove_entry.get())
    except:
        return


    remove_entry.delete(0,'end')
    m.remove_song(element)

    cur = 0
    for i in ids:
        if i==element:
            ids.pop(cur)
            list.pop(cur).destroy()
            cur-=1
            break;
        cur+=1
    i = 2
    for j in range(len(list)):
        if j >= len(list) - 5:
            list[j].grid(row=i, column=0)
            i += 1


remove_button = Button(remove_frame, text="Remove",command=rem)
remove_button.grid(row=2,column=0)


submit = Button(add_song,text="Submit", command = submit)
submit.grid(row=2,column=2)


filtered = []
filtered_frame = LabelFrame(root)
filtered_frame.grid(row=4,column=0)
def filt():
    art = artist_entry.get()
    gen = genre_entry.get()
    if art == '':
        art = None
    if gen == '':
        gen = None

    min_listens = min_listen_entry.get()
    if min_listens!='':
        min_listens = int(min_listens)
    else:
        min_listens = 0

    max_listens = max_listen_entry.get()
    if max_listens!='':
        max_listens = int(max_listens)
    else:
        max_listens = sys.maxint

    min_likes = min_like_entry.get()
    if min_likes!='':
        min_likes = int(min_likes)
    else:
        min_likes = 0

    max_likes = max_like_entry.get()
    if max_likes!='':
        max_likes = int(max_likes)
    else:
        max_likes = sys.maxint
    temp = m.filter(art,gen,min_listens,max_listens,min_likes,max_likes,sort_by, order)
    #destroy previous labels
    for i in range(len(filtered)):
        filtered.pop().destroy()

    #add new labels
    i=0
    for row in temp:
        s = "Song iD: " + str(row[0]) + "  Title: " + str(row[1]) + " " + "  Artist: " + str(row[2]) + "  Genre: " + str(
        row[3]) + "  Listens: " + str(row[4]) + "  Likes: " + str(row[5])
        lab = Label(filtered_frame,text=s)
        lab.grid(row=i,column=0)
        i+=1
        filtered.append(lab)





filter_button = Button(filter,text="Filter", command = filt)
filter_button.grid(row=2,column=0,columnspan=6)

root.mainloop()