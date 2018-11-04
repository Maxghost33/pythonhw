import random

rang = int(input("Choose size of battlefield: "))

def print_board(board):
    for row in board:
        print(" ".join(row))

def graph_board(board, row, col, value):
    board[row - 1][col - 1] = value

def random_row(board):
    return random.randint(1, len(board))

def random_col(board):
    return random.randint(1, len(board[0]))


def play(board):
    print("Let's play Battleship!")
    print_board(board)

    ship_row = random_row(board)
    ship_col = random_col(board)
    print(ship_row * 2)
    print(ship_col * 2)
    turn = 1
    for turn in range(rang+1):
        turn = turn
        print("Attempt# " +  str(turn)) 
        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))
        
        if guess_row == ship_row and guess_col == ship_col:
            graph_board(board, guess_row, guess_col, "X")
            print_board(board)
            print("Congratulations! You sunk my battleship!")
            break
        if (guess_row <= 0 or guess_row > rang) or (guess_col <= 0 or guess_col > rang):
            print("Oops, that's not even in the ocean. Try again!")
        else:
            if (board[guess_row - 1][guess_col - 1] == "o"):
                print_board(board)
                print("You guessed that one already. Try again!")
            else:
                if turn == rang:
                    graph_board(board, guess_row, guess_col, "o")
                    print_board(board)
                    print("Game Over. You are loser!")
                    break
                else:
                    graph_board(board, guess_row, guess_col, "o")
                    print_board(board)
                    print("You missed my battleship! Try again!")

def main():
    board = []
    for x in range(rang):
        board.append(["*"] * rang)
    #print (board)
    play(board)


if __name__ == "__main__":
    main()   
