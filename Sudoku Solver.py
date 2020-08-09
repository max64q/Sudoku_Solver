#Sudoku Solver

import numpy as np

board = np.array([[0, 0, 0, 8, 4, 0, 0, 0, 3],
                  [0, 7, 5, 0, 0, 0, 0, 0, 0],
                  [0, 4, 3, 0, 0, 6, 0, 0, 0],
                  [0, 0, 7, 0, 0, 8, 4, 9, 0],
                  [0, 0, 0, 9, 3, 1, 0, 0, 0],
                  [0, 5, 2, 7, 0, 0, 8, 0, 0],
                  [0, 0, 0, 2, 0, 0, 3, 4, 0],
                  [0, 0, 0, 0, 0, 0, 6, 2, 0],
                  [2, 0, 0, 0, 7, 3, 0, 0, 0]])




#check if input is viable solution for a cell
def isSolution(row, col, n):
    #returns 1 for true (solution) and 0 for false (not solution)
    #print("checking solution")
    a = np.where(board[row,:] == n) #indicies of ns in row
    b = np.where(board[:,col] == n) #indicies of ns in column
    if((a[0].size + b[0].size) == 0): #checks that a and b are empty sets
        if(checkHouse(row, col, n) == 0):
            #print("solution true")
            return 1
        else:
            return 0
    else:
        return 0
      
#check if given number is present in house
def checkHouse(row, col, n):
    #have to cycle through each combination of 2 equations 
    #equation 1 => 1 - 2(x != 0)||equation 2 => 2 - x^2
    #to check each other square in house
    #print('checkHouse')
    if(board[(row + eq1(row)), (col + eq1(col))] == n): #1,1
        return(1) #returns 1 if number is repeated in house
    elif(board[(row + eq1(row)),(col + eq2(col))] == n): #1,2
        return(1)
    elif(board[(row + eq2(row)),(col + eq1(col))] == n): #2,1
        return(1)
    elif(board[(row + eq2(row)),(col + eq2(col))] == n): #2,2
        return(1)
    else:
        return(0)

#equation 1 for checking house
def eq1(x):
    x = x % 3
    #(0,1,2) -> (1, -1, -1)
    return(1 - (2 * (x != 0)))

#equation 2 for checking house
def eq2(x):
    x = x % 3
    #(0,1,2) -> (2, 1, -2)
    return(2 - x**2)

#solve
def solve():
    for row in range(0, 9): #iterate through rows
        for col in range(0,9): #iterate through columns
            if(board[row, col] == 0):
                for n in range(1, 10):
                    #print("row = ", row, "col = ", col, "n = ", n)
                    if(isSolution(row, col, n)):
                        board[row,col] = n
                        print(board)
                        solve()
                        #function is returned when no n is found to be solution
                        board[row,col] = 0
                    
                    
                return 
        

    print(board)
#main
solve()
print(board)




    
    
    
    
    
    
    