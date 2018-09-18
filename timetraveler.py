#nswe
tilematrix = ["n","nse","se","we","sw","n","sw","ns","n"]
n = 0
m = 0
diravailable = ''

for i in tilematrix:
    diravailable = ''
    for j in tilematrix[n]:
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
    n += 1
    print(diravailable)

