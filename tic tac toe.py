board = [' ' for x in range(10)]

def insert_letter(letter, pos):
    board[pos] = letter

def SpaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |   ')
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("   |   |   ")
    print("-----------")
    print('   |   |   ')
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("   |   |   ")
    print("-----------")
    print('   |   |   ')
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def IsWinner(board , letter):
    f1 = (board[1] == letter and board[2] == letter and board[3] == letter)
    f2 = (board[4] == letter and board[5] == letter and board[6] == letter)
    f3 = (board[7] == letter and board[8] == letter and board[9] == letter)
    f4 = (board[1] == letter and board[4] == letter and board[7] == letter)
    f5 = (board[2] == letter and board[5] == letter and board[8] == letter)
    f6 = (board[3] == letter and board[6] == letter and board[9] == letter)
    f7 = (board[1] == letter and board[5] == letter and board[9] == letter)
    f8 = (board[3] == letter and board[5] == letter and board[7] == letter)
    f = f1 or f2 or f3 or f4 or f5 or f6 or f7 or f8
    return f

def playerMove():
    run = True
    while  run:
        move = input("Please select a position to enter the X between 1 to 9")
        try:
            move = int(move)
            if move > 0 and move <10:
                if SpaceIsFree(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print("Sorry , this space is occupied")

            else:
                print("Please type a no. between 1 and 9")

        except:
            print("Please type a number")

def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == " " and x!=0]
    move =0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    corneropen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            corneropen.append(i)

    if len(corneropen) > 0:
        move = selectRandom(corneropen)
        return corneropen[move]

    if 5 in possibleMoves:
        move = 5
        return  move

    edgesopen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesopen.append(i)

    if len(edgesopen) >0:
        move = selectRandom(edgesopen)
        return edgesopen[move]
    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return r

def main():
    print("welcome to the game!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(IsWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry you lose!")
            break
        if not(IsWinner(board, 'X')):
            comp_move = computerMove()
            if comp_move == 0:
                print(" ")
            else:
                insert_letter('O', comp_move)
                print('Computer placed an O on position ', comp_move , ':')
                printBoard(board)

        else:
            print("YOU WIN")
            break

    if isBoardFull(board):
        print("Tie Game")

while True:
    x = input("Do you want to play again? (y/n) ")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------------')
        main()
    else:
        break