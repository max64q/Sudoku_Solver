import numpy as np

board = np.array([[0, 0, 9, 0, 5, 0, 0, 4, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 7, 0, 0, 5, 1, 6],
                  [0, 0, 3, 0, 0, 0, 1, 7, 0],
                  [1, 0, 0, 0, 0, 0, 0, 3, 2],
                  [0, 4, 8, 0, 0, 0, 0, 0, 0],
                  [2, 0, 0, 0, 0, 5, 8, 0, 0],
                  [0, 8, 0, 0, 2, 1, 6, 0, 0],
                  [3, 9, 0, 0, 0, 0, 0, 0, 0]])

#check if input is viable solution for a cell
def isSolution(row, col, n):

    for i in range(0,9):
        if(board[row,i] == n):
            return False
        if(board[i,col] == n):
            return False
    h = (1 - (2 * ((row % 3) != 0)))
    i = (1 - (2 * ((col % 3) != 0)))
    j = (2 - (row % 3)**2)
    k = (2 - (col % 3)**2)
    if(board[row + h, col + i] == n):
        return False
    elif(board[row + h, col + k] == n):
        return False
    elif(board[row + j, col + i] == n):
        return False
    elif(board[row + j, col + k] == n):
        return False
    else:
        return True
    

def solve():
    for row in range(0, 9):
        for col in range(0,9):
            if(board[row,col] == 0):
                for n in range(1, 10):
                    if(isSolution(row, col, n)):
                        board[row,col] = n
                        if (board != 0).all():
                            raise StopIteration
                        solve()
                        board[row,col] = 0

                return


#main
try:
    solve()
except StopIteration:
    print(board)
