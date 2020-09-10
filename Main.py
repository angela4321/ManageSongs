from Manage import Manage

m = Manage()
num = 0
while True:
    print("Current songs:")
    s = m.get_songs()
    for row in s:
        print(row)
    print("Type A to add a song R to remove and F to finish")
    inp = input()
    if inp=='F':
        break
    if inp == "A":
        num+=1
        print("Type in the Title, Artist, Number of Listens, and Number of Likes in order separated by spaces")
        inp = input()
        arr = inp.split(" ")
        m.add_song(num,arr[0],arr[1],arr[2],arr[3])
    elif inp == "R":
        print("Type in the ID of the song you would like to remove")
        inp = int(input())
        m.remove_song(inp)






m.close()

