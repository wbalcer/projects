import time


def refresh(board):
    print_board(board)
    print()
    print()
    print()
    time.sleep(0.5)

def solve(board):
  for i in range(9):
    for j in range(9):
      if board[i][j] == 0:
        for k in range(1, 10):
          if is_valid(board, i, j, k):
            #Place the number and recurse to solve the rest of the board
            board[i][j] = k
            refresh(board)
            solve(board)
            #If the board is not solvable, backtrack and try a different number
            board[i][j] = 0
            refresh(board)
        return
  print("Solution:")
  print_board(board)

def is_valid(board, row, col, num):
  #Check if the number is already in the row
  for i in range(9):
    if board[row][i] == num:
      return False
  #Check if the number is already in the column
  for i in range(9):
    if board[i][col] == num:
      return False
  #Check if the number is already in the 3x3 square
  start_row = row - row % 3
  start_col = col - col % 3
  for i in range(3):
    for j in range(3):
      if board[start_row + i][start_col + j] == num:
        return False
  #If the number is not in the row, column, or subgrid, it is valid
  return True

def print_board(board):
  for i in range(9):
    for j in range(9):
      print(board[i][j], end=' ')
    print()

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
refresh(board)
solve(board)


