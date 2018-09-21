'''
Hópur 2:
Anna Dóra Aldísardóttir
Gözde Sigurðs
Izabela Kinga Nieradko
Jóhann Sveinn Ingason
Marinó Guðmundsson

1. Which implementation was easier and why?
    Since it´s based on the first program. Making the second program was
    easier since we already solved the problem, we just improved our solution.
    One way to look at it is that the first program was a draft, an algorithm we could implement into our second program.

2. Which implementation is more readable and why?
    The second one, is a lot more readable because of the functions. 
    By sectioning the program, it becomes less intimidating and not as much of a clutter. 
    It can be hard for anyone other than the original programmers to read this kind of code since they would have to spend more time analyzing how it works. 

3. Which problems in the first implementations were you able to solve with the latter implementation?
    Beside the problem of overall readability, the new program makes it easier for us to make another similar program based on this one by using the functions. 
    We didn't have to repeat code that we already wrote to make it work.

N = +1
E = +3
W = -3
S = -1
'''

def move(available_directions, location, direction): #Function that moves the player and returns current location
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

def is_winner(location): #If location == 6 then we have a winner.
    if location == 6:
        return True
    return False

def print_available_directions(available_directions): #Function checking all available direction player can move to
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

def play(): #Function with a while loop that allows us to play the game and puts other functions to use.
    tilematrix = "n nes es n ws ew n ns ws"
    tilematrix_split = tilematrix.split()
    location = 0

    while True:
        print_available_directions(tilematrix_split[location])

        direction = input("Direction: ")
        location = move(tilematrix_split[location], location, direction)

        if is_winner(location):
            print("Victory!")
            break

play()