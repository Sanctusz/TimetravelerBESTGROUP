""" 
To solve the tile traveler problem we first needed to look at it from x and y axis perspective.
The grid 3x3 so the player can travel at most +3 or -3 back
Therefore n+=3, n-=3. But because of wall we had to take into consideration that player may only be able to move 
n +=1 and n -= 1
Every tile on the has different cordinates and different possible ways to go. 
We have to mark the possition of a player then put it into a loop so we can be updated on the possition player 
is on the grid.
the winning tile would have number 6 as player has to go +1(north) +1 (north) +3 (east) +3(east) -1(south) -1(south)
which equal 6.

 """
'''
N = +1
E = +3
W = -3
S = -1
'''

timematrix = ("n nes es n ws ew n ns ws") # all available directions player can go

timematrix_split = timematrix.split() #changing string into list

n = 0 #location of player
m = 0 #checks the contest of diravailable
diravailable = '' #creating new string

for i in timematrix_split: #for loop thats checks which direction player can travel
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
        print("WINNER!")
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
        #n += 1
        #print(diravailable)