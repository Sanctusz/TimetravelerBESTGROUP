#news
'''
N = +1
E = +3
W = -3
S = -1
'''

def move(available_directions, location, direction): # function that moves the player and returns current location
    direction = direction.lower()
    if direction in available_directions:
        if direction == "n":
            location += 1
        elif direction == "e":
            location += 3
        elif direction == "w":
            location -= 3
        elif direction == "s":
            location -= 1

    return location

def is_winner(location): #if location == 6 then we have a winner.
    if location == 6:
        return True
    return False

def print_available_directions(available_directions): #function checking all available direction player can move to
    text = ''
    first = True

    for direction in available_directions:
        if direction == "n":
            text = "You can travel: (N)orth"
        elif direction == "s":
            if first:
                text = "You can travel: (S)outh"
            else:
                text += " or (S)outh"
        elif direction == "w":
            if first:
                text = "You can travel: (W)est"
            else:
                text += " or (W)est"
        elif direction == "e":
            if first:
                text = "You can travel: (E)east"
            else:
                text += " or (E)ast"
        first = False
    print(text)

def play(): # function with a while loop that's allows us to play the game and puts other functions to use.

    tilematrix = ("n nes es n ws ew n ns ws")
    tilematrix_split = tilematrix.split()
    location = 0

    while True:
        print_available_directions(tilematrix_split[location])

        direction = input("Direction: ")
        location = move(tilematrix_split[location], location, direction)

        if is_winner(location):
            print("WINNER!")
            break
        
        


play()