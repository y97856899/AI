red = "X"
blue = "O"

def terminal(board, left, last):
    """Checks if the game is over."""
    if winner(board) is not None:
        
        return True
    
    if last[0] and last[1]:   
        
        return True
    
    for count in left[red].values():  
        
        if count != 0:
            return False

    for count in left[blue].values():
        if count != 0:
           return False

    return True


def winner(board):
    """Returns the winner of the game, if there is one."""
    rows = board + get_columns(board) + get_diagonal(board)
    
    for row in rows:
        if three_in_a_row(row):
            
            return row[0][0]  
        
    return None

def get_columns(board):
    """Returns all columns of the board."""
    columns = []
    for j in range(3):
        
        column = []
        for i in range(3): 
             column.append(board[i][j])
             
        columns.append(column)
        
        
    return columns


def get_diagonal(board):
    """Returns the two diagonals of the board."""
    
    first = []
    second = []
    
    for i in range(3):
        first.append(board[i][i])
        
    for i in range(3):
        second.append(board[i][2 - i])

    return [first, second]


def three_in_a_row(row):
    """Checks if all elements in a row are the same and not None."""
    if row[0][0] is None:  
        
        return False
    
    for cell in row:
        if cell[0] != row[0][0]: 
            
            return False
    return True

   

def player(turn):          #I change to know which player will play by if even for X,if odd for O
    """Returns the player who has the next turn on a board."""
    return red if turn % 2 == 0 else blue




def actions(board, left, player):
    """Returns all possible actions on the board."""
    actions = set()
    
   
    sizes = {1, 2, 3}

    
    for i in range(len(board)):
        for j in range(len(board[i])):
            
            marker = board[i][j][0]  
            height = board[i][j][1]  
            
            
            if marker is None:  
                
                  actions.add((i, j))
                  
            elif marker != player and height < 3:  
                
                  if any(left[player][size] > 0 for size in sizes): 
                      
                      
                        actions.add((i, j))

    return actions



from copy import deepcopy
def result(board, action, pieces, piecesLeft, current):
    """Returns the board after making the given move."""
    i, j = action
    marker = board[i][j][0]  
    height = board[i][j][1]  
    
    
    if  marker is None:
        newBoard = deepcopy(board)
        
        newPieces = deepcopy(piecesLeft)
        newBoard[i][j] = (current, pieces)
        
        
        
        newPieces[current][pieces] -= 1  
        
        return newBoard, newPieces
    
  
    if height == 3:
        return False  

    
    if pieces <= height:
        return False  

    
    newSize = max(pieces, height)  
    newBoard = deepcopy(board)
    
    
    newPieces = deepcopy(piecesLeft)

    newBoard[i][j] = (current, newSize)  
    
    newPieces[current][pieces] -= 1  
    
    
    return newBoard, newPieces




def utility(board):    
    """Returns the utility value of the board."""
    win = winner(board)
    if win == red:
        
        return 1
    elif win == blue:
        return -1
    return 0




def board1(board):
    for row in board:
        print([
            f"{'red' if cell[0] == 'X' else 'blue' if cell[0] == 'O' else ' '}|(size={cell[1]})"
            for cell in row
        ])



def main():
    """Main function to play the game."""
    board = [[(None, 0), (None, 0), (None, 0)],
             [(None, 0), (None, 0), (None, 0)],
             [(None, 0), (None, 0), (None, 0)]]  

    
    piecesL = {
        red: {1: 2, 2: 2, 3: 2},  
        blue: {1: 2, 2: 2, 3: 2}   
    }

    turn = 0  
    last = [False, False]  

    print("Welcome to Tic Tac Toe higher level!")
    print("You are 'O'. AI is 'X'.")
    print("Enter your moves as row, column, and size (0 or 1 or 2).")

    over = True  

    while not terminal(board, piecesL, last) and over:
        print("\nCurrent Board:")
        
        
        board1(board)
        

        current = player(turn)

        if current == blue:
            print("Your turn!")
            
            
            while True:
                try:
                    row, col, size = map(int, input("Enter row, column, and the size (1, 2, or 3): ").split())
                    
                    move = result(board, (row, col), size, piecesL, blue)
                    
                    if move:
                        board, piecesL = move
                        
                        last[0] = False  
                        break
                    else:
                        print("Invalid move. You cannot place a smaller piece or overwrite a size. Try again.")


                except ValueError:
                    print("Invalid input. Please enter three integers separated by spaces.")
        
        else:
            print("AI's turn!")
            ai_passed = True
            for action in actions(board, piecesL, red):
                
                for size in [1, 2, 3]:
                    
                    
                    if piecesL[red][size] > 0 and board[action[0]][action[1]][1] + size <= 3:
                        
                        
                        result_move = result(board, action, size, piecesL, red)
                        
                        if result_move:
                            board, piecesL = result_move
                            
                            print(f"AI chose: {action} with size {size}.")
                            
                            
                            last[1] = False  
                            ai_passed = False
                            
                            break
                if not ai_passed:
                    
                    break


        
        winnerPlayer = winner(board)
        if winnerPlayer:  
            print("\nFinal Board:")
            board1(board)
            break  

        turn += 1  
  

    if winnerPlayer == red:
        print("\nAI wins!")
    elif winnerPlayer == blue:
        print("\nCongratulations! You win!")
    else:
        print("\nIt's a draw!")




if __name__ == "__main__":
    main()
