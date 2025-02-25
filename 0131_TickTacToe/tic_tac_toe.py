# Tic tac toe game
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

def create_new_board():
    mat=[]
    for i in range(3):
        rowList = []
        for j in range(3):
            rowList.append("-")
        mat.append(rowList)
    return mat

board = create_new_board()

def show_board(board):
    print("This is the actual board:")
    for row in board:
        print(row)

def display_rules():
    print("")
    print("Rules for Tic-Tac-Toe")
    print("Players take turns putting their marks in empty squares. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
    print("")

def choose_player():
    print("")
    print("")
    print("TIC TAC TOE the most well known game in the world !!!!")
    print("This is a game for two players")
    print("Please Enter the name of the first Player: ")
    Player1 = input()
    print("What symbol would you like to use", Player1, "? The choices are only X or 0")
    Player1_symbol = input()
    while (isnotvalid(Player1_symbol)):
       #ask again
       print("Nice try ",Player1,". Please only X or O.")
       Player1_symbol = input()
    print("Please Enter the name of the second Player: ")
    Player2 = input()
    Player2_symbol=choose_player2_symbol(Player1_symbol)
    print("Thah means that", Player2, "will be playing ", Player2_symbol)
    return [Player1,Player1_symbol,Player2,Player2_symbol]

def isnotvalid(symbol):
    if symbol != "X":
        if symbol != "O":
            return True
    else:
        return False

def choose_player2_symbol(Player1_symbol):
    if Player1_symbol == "X":
        Player2_symbol = "O"
    else:
        Player2_symbol = "X"
    return Player2_symbol

def is_board_full(board):
    #if (one single cell is empty)
    for row in board:
        for cell in row:
            if cell == "-":
                return False
    else:
        return True

def check_win(board):
    #algorithm TicTacToeWinTest(A):
    ''' INPUT
        A = a state of the tic-tac-toe board where each cell can be a - or filled with X or O
        OUTPUT
        true if A represents a win for either player; false if A is not a win'''
    # Find the player(s) that connected three cells
    # Check the rows and columns
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "-":
            return True
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] != "-":
            return True

    # Check the diagonals
    if board[0][0] == board[1][1] == board [2][2] and board [0][0] != "-":
        return True
    if board[2][0]==board[1][1]==board[0][2]and board[2][0] !="-":
            return True
    else:
        return False

def take_player_move(board,Player,Players_symbol):
    #Input player's move as row and column numbers.
    #returns the updated board
    #first we will assume that the cell is empty
    if not(is_board_full(board)):
        Cell_is_empty = True
            #as long as the cell is empty:
        while Cell_is_empty:
            print("First, select your row (Just between 1 and 3):")
            row=int(input())-1
            while (row < 0 or row > 2):
                print ("Please enter a number between 1 and 3")
                row=int(input())-1
            print("now, please select the column")
            column=int(input())-1
            print(Player,"choosed",row,",",column)
            while (column < 0 or column > 2):
                print ("Please enter a number between 1 and 3")
                column=int(input())-1
            #- Check if the chosen cell is empty:
                # - If empty, place the player's symbol in that cell.
            if board[row][column] == "-":
                    board[row][column] = Players_symbol
                    return board
            else:
            # If not empty, prompt the player to choose another cell.
                print("Soryyyy!!!!That cell is already choosen, please choose another")
        Cell_is_empty = False
    else:
        print("Board is full!!")
        return board

def game_loop(players_and_symbols,board):
    Player1 = players_and_symbols[0]
    Player2 = players_and_symbols[2]
    Player1_symbol = players_and_symbols[1]
    Player2_symbol = players_and_symbols[3]
    #- Start the game with Player 1.
    print (Player1, " Please enter your move")
    board = take_player_move(board,Player1,Player1_symbol)
    show_board(board)
    #after the first move
    current_player = Player1
    current_player_symbol = Player1_symbol
    #while game is not full and there is not a winner
    while not(is_board_full(board)) and not(check_win(board)):
        #switch players
        if current_player == Player1:
            current_player = Player2
            current_player_symbol = Player2_symbol
        else:
            current_player = Player1
            current_player_symbol = Player1_symbol
        print("It is ",current_player,",(",current_player_symbol,") turn")
        #take player move
        board = take_player_move(board,current_player,current_player_symbol)
        #display board
        show_board(board)
    if check_win(board):
            print ("Congratulatations ",current_player,"you won !!!!!!")
            #break
    else:
        #declare tie
        print("There is no winner!!! We have a tie")
    
def wanna_play_again():
    print("That was nice!!, would you like to play again? [Y] or [N]")
    answer = input()
    while answer != "Y" and answer != "N":
        print("Please enter [Y] or [N]")
        answer = input()
    if answer == "Y":
        return True
    else:
        return False

def end_game():
    print("Thank you for playing, till next time Champions")

players_and_symbols = choose_player()
display_rules()
show_board(board)
game_loop(players_and_symbols,board)
while wanna_play_again():
    board = create_new_board()
    players_and_symbols = choose_player()
    show_board(board)
    game_loop(players_and_symbols,board)
end_game()

# Tic-tac-toe game
if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    #ask for a new game

#--------------------------------------------------
