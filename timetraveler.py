#news
tilematrix = ["n","nes","es","ew","ws","n","ws","ns","n"]
n = 0
m = 0
diravailable = ''

for i in tilematrix:
    diravailable = ''
    m = 0
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