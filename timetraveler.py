'''
Hópur 2:
Anna Dóra Aldísardóttir
Gözde Sigurðs
Izabela Kinga Nieradko
Jóhann Sveinn Ingason
Marinó Guðmundsson

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
W = -3
S = -1
'''

timematrix = "n nes es n ws ew n ns ws" # all available directions player can go

timematrix_split = timematrix.split() #changing string into list

n = 0 #location of player
m = 0 #checks the contest of diravailable
diravailable = '' #creating new string

for i in timematrix_split: #for loop that checks which directions player can travel
        diravailable = ''
        m = 0
        for j in timematrix_split[n]:
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

while n != 6: #while loop thats check the position of a player and updates it.
    print(diravailable)
    way = input("Direction: ")
    if way in timematrix_split[n]:
        if way == "n":
            n += 1
        elif way == "e":
            n += 3
        elif way == "w":
            n -= 3
        elif way == "s":
            n -= 1
    if n == 6:
        print("Victory!")
        break
    for i in timematrix_split: #for loop that checks the updated player position 
        diravailable = ''
        m = 0
        for j in timematrix_split[n]:
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