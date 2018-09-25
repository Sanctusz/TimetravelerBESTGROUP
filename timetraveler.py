'''
Hópur 2:
Anna Dóra Aldísardóttir
Gözde Sigurðs
Izabela Kinga Nieradko
Jóhann Sveinn Ingason
Marinó Guðmundsson

github repo: https://github.com/Sanctusz/TimetravelerBESTGROUP.git

You need to get to point 6 in the list.
You start at point 0.
When you go North you go up 1 slot in the list.
When you go East you go up 3 slots in the list.
When you go West you go down 3 slots in the list.
When you go South you go down 1 slot in the list.
There are walls which you can't go through.
If you try and go into a direction you can't go then you get an error.
Find your way through the maze.

N = +1
E = +3
S = -1
W = -3
'''

<<<<<<< HEAD
string = "n nes es n ws ew n ns ws"
tilematrix = string.split(' ')
#tilematrix = ["n","nes","es","n","ws","ew","n","ns","ws"]
n = 0 #location of player
m = 0 #
diravailable = ''
=======
tilematrix = "n nes es n sw ew 1 ns sw" # all available directions player can go

tilematrix_split = tilematrix.split() #changing string into list

#create our variables
n = 0 
m = 0 
diravailable = '' 
>>>>>>> 52efea0515de2d26d964b3daeecab1dd8af88e95

for i in tilematrix_split: #for loop outputs possible routes the player can take. Need one outside the loop in the beginning.
    diravailable = ''
    m = 0
    for j in tilematrix_split[n]:
        if j == "n":
            diravailable = "You can travel: (N)orth"
        elif j == "s":
            if m == 0:
                diravailable = "You can travel: (S)outh"
            else:
                diravailable += " or (South)"
        elif j == "w":
            if m == 0:
                diravailable = "You can travel: (W)est"
            else:
                diravailable += " or (W)est"
        elif j == "e":
            if m == 0:
                diravailable = "You can travel: (E)east"
            else:
                diravailable += " or (E)ast"
        m += 1
print(diravailable + '.')

while n != 6: #while loop thats check the position of a player and updates it.
    way = input("Direction: ").lower()
    if way in tilematrix_split[n]:
        if way == "n":
            n += 1
        elif way == "e":
            n += 3
        elif way == "w":
            n -= 3
        elif way == "s":
            n -= 1
        for i in tilematrix_split: #for loop outputs possible routes the player can take
            diravailable = ''
            m = 0
            for j in tilematrix_split[n]:
                if j == "n":
                    diravailable = "You can travel: (N)orth"
                elif j == "s":
                    if m == 0:
                        diravailable = "You can travel: (S)outh"
                    else:
                        diravailable += " or (S)outh"
                elif j == "w":
                    if m == 0:
                        diravailable = "You can travel: (W)est"
                    else:
                        diravailable += " or (W)est"
                elif j == "e":
                    if m == 0:
                        diravailable = "You can travel: (E)ast"
                    else:
                        diravailable += " or (E)ast"
                m += 1
        if n == 6:
            print("Victory!")
            break
        print(diravailable + '.')
    else:
        print("Not a valid direction!")