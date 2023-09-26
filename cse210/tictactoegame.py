'''
Tic-Tac-Toe Game
Author: Flavia Santos Bezerra
'''
A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7
H = 8
I = 9
live = 1 
turn = "x"
draw = 0


def Board():
    global A 
    global B 
    global C 
    global D 
    global E 
    global F 
    global G 
    global H 
    global I
    print (f"{A}|{B}|{C}\n-+-+-\n{D}|{E}|{F}\n-+-+-\n{G}|{H}|{I}")

def WinLose():
    global A 
    global B 
    global C 
    global D 
    global E 
    global F 
    global G 
    global H 
    global I
    global live
    global turn
    global draw

    if (A == B == C or  D == E == F or G == H == I 
    or A == D == G or  B == E == H or C == F == I
    or A == E == I or  C == E == G):
        print(f"{turn} Wins!")
        print ("Good game! Thanks for playing!")
        live = 0

    if draw == 9:
        print ("draw!")
        print ("Good game! Thanks for playing!")
        live = 0


    
def main():
    global A 
    global B 
    global C 
    global D 
    global E 
    global F 
    global G 
    global H 
    global I 
    global live  
    global turn
    global draw
    Board()

    while live == 1:
        number = int(input(f" {turn}'s turn to choose a square (1-9): "))
        if number == 1:
            A = turn
        if number == 2:
            B = turn
        if number == 3:
            C = turn
        if number == 4:
            D = turn
        if number == 5:
            E = turn
        if number == 6:
            F = turn
        if number == 7:
            G = turn
        if number == 8:
            H = turn
        if number == 9:
            I = turn
        
        Board()
        draw += 1
        WinLose()
        if turn == "x":
            turn = "o"
        else:
            turn = "x"
        
    return

if __name__ == "__main__":
    main()