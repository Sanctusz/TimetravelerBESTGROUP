posx = 2
posy = 3

maxpos = 3
minpos = 1
#3,1 win tile
#nswe
tilematrix = ["n","nse","ne","we","sw","n","sw","ns","n"]
n = 0
m = 0
diravailable = ''

for i in tilematrix:
    print(n, tilematrix[n])
    for j in tilematrix[n]:
        m += 1
        if j == "n":
            diravailable = "You can travel: (N)orth"
        elif j == "s":
            if m == 1:
                diravailable = "You can travel: (S)outh"
            else:
                diravailable += diravailable + "or (South)"
        elif j == "w":
            if m == 1:
                diravailable = "You can travel: (W)est"
            else:
                diravailable += diravailable + "or (W)est"
        else:
            if m == 1:
                diravailable = "You can travel: (E)east"
            else:
                diravailable += diravailable + "or (E)ast"
    n += 1

for i in range(0,9):
    n += 1
    print(diravailable)

'''
if posx == 1 and posy == 1:
    print(tilematrix[0])
elif posx == 1 and posy == 2:
    print(tilematrix[1])
elif posx == 1 and posy == 3:
    print(tilematrix[2])
'''
if posx == 3 and posy == 1:
    print("winner!!")