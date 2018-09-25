#news
'''
N = +1
E = +3
W = -3
S = -1
'''

string = "n nes es n ws ew n ns ws"
tilematrix = string.split(' ')
#tilematrix = ["n","nes","es","n","ws","ew","n","ns","ws"]
n = 0 #location of player
m = 0 #
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

while n != 6:
    print(diravailable)
    way = input("Direction: ")
    if way in tilematrix[n]:
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
        #n += 1
        #print(diravailable)