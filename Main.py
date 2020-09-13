from Manage import Manage

m = Manage()
num = 0
while True:
    print("Current songs:")
    s = m.get_songs()
    for row in s:
        print(row)
    print("Type A to add a song R to remove L to get songs by letter S to sort ART to get songs by an Artist LIKE to get songs by likes and F to finish")
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
    elif inp == "L":
        print("Type the first letter of the song you are looking for")
        inp = input()
        temp = m.letter(inp)
        for row in temp:
            print(row)
    elif inp == "S":
        print("Type ASC to sort by ascending and DESC to sort by descending")
        inp1 = input()
        print("Type NUM_LISTENS to sort by number of listens and NUM_LIKES to sort by number of likes")
        inp2 = input()
        temp = m.sort(inp1,inp2)
        for row in temp:
           print(row)
    elif inp=='ART':
        print("Type the artist name")
        inp = input()
        temp = m.get_artist(inp)
        for row in temp:
            print(row)
    elif inp == "LIKE":
        print("What is the min number of likes?")
        inp1 = input()
        print("What is the max number of likes?")
        inp2 = input()
        temp = m.get_song_by_likes(inp1,inp2)
        for row in temp:
            print(row)
    print("\n")

m.close()

