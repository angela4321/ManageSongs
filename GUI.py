from tkinter import *
from Manage import Manage

m = Manage()


root = Tk()
label1 = Label(root,text="Title")
label1.grid(row=0,column=0)
entry1 = Entry(root,width=20)
entry1.grid(row=1,column=0)

label2 = Label(root,text="Artist")
label2.grid(row=0,column=1)
entry2 = Entry(root,width=20)
entry2.grid(row=1,column=1)

label3 = Label(root,text="Genre")
label3.grid(row=0,column=2)
entry3 = Entry(root,width=20)
entry3.grid(row=1,column=2)

label4 = Label(root,text="Listens")
label4.grid(row=0,column=3)
entry4 = Entry(root,width=20)
entry4.grid(row=1,column=3)

label5 = Label(root,text="Likes")
label5.grid(row=0,column=4)
entry5 = Entry(root,width=20)
entry5.grid(row=1,column=4)

list = []
id = 0
def submit():
    global id
    id+=1
    title = entry1.get()
    artist = entry2.get()
    genre = entry3.get()
    listens = entry4.get()
    likes = entry5.get()
    m.add_song(id,title,artist,genre,listens,likes)
    temp = m.get_songs()
    i = 2
    for row in temp:
        i+=1
        s = "Title: "+str(row[0])+" "+"Artist: "+str(row[1])+"Genre: "+str(row[2])+"Listens: "+str(row[3])+"Likes: "+str(row[4])
        lab = Label(root,text=s)
        lab.grid(row=i,column=0)

submit = Button(root,text="Submit", command = submit)
submit.grid(row=2,column=2)
root.mainloop()