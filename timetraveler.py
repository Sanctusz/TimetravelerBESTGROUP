#news
'''
N = +1
E = +3
W = -3
S = -1
'''

timematrix = ("n nes es n ws ew n ns ws")

timematrix_split = timematrix.split()

n = 0 #location of player
m = 0 #
diravailable = ''

for i in timematrix_split:
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

while n != 6:
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
    for i in timematrix_split:
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