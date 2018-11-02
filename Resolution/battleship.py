import random

rang = int(raw_input("Choose size of battlefield: "))



def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return random.randint(0, len(board) - 1)

def random_col(board):
    return random.randint(0, len(board[0]) - 1)


def play(board):
    print "Let's play Battleship!"
    print_board(board)

    ship_row = random_row(board)
    ship_col = random_col(board)
    print ship_row * 2
    print ship_col * 2
    turn = 0
    for turn in range(5):
        turn = turn + 1
        print "Attempt#", turn 
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))

        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk my battleship!"
            break
        else:
            if (guess_row < 0 or guess_row > rang) or (guess_col < 0 or guess_col > rang):
                print "Oops, that's not even in the ocean."
            #elif(board[guess_row][guess_col] == "X"):
            #    print "You guessed that one already."
            else:
                if turn == rang:
                    print "Game Over"
                    break
                else:
                    print "You missed my battleship!"
                    #board[guess_row][guess_col] = "X"
                    print_board(board)


def main():
    board = []
    for x in range(rang):
        board.append(["O"] * rang)
    play(board)


if __name__ == "__main__":
    main()   
