#Programming for the Puzzled -- Srini Devadas
#A Profusion of Queens
#Given the dimension of a square "chess" board, call it N, find a placement
#of N queens such that no two Queens attack each other using recursive search

#This procedure initializes the board to be empty, calls the recursive N-queens
#procedure and prints the returned solution
def nQueens(size, location = None):
    board = [-1] * size
    if location == None: location = board.copy()
    rQueens(board, 0, size, location)
    print(board)
    printBoard(board)

#This procedure checks that the most recently placed queen on column current
#does not conflict with queens in columns to the left.
def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        if (current - i == abs(board[current] - board[i])):
            return False
    return True 


#This procedure places a queens on the board on a given column so it does
#not conflict with the existing queens, and then calls itself recursively
#to place subsequent queens till the requisite number of queens are placed
def rQueens(board, current, size, location):
    if (current == size):
        return True
    else:
        for i in range(size):
            if location[current] == -1:
                board[current] = i
            else: board[current] = location[current]
            
            if (noConflicts(board, current)):
                done = rQueens(board, current + 1, size, location)
                if (done):
                    return True
        return False


def printBoard(board):
    size = len(board)
    
    for i in range(size):
        queen = board.index(i)
        print('. '*queen + 'Q ' + '. '*(size-queen-1))
                    
nQueens(20)
nQueens(10,[-1, -1, 4, -1, -1, -1, -1, 0, -1, 5])