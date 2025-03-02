# Function to find the next empty spot (represented by 0)
def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

# Function to check if placing a number is valid
def is_valid(board, num, row, col):
    # Check the row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

# Backtracking solver function
def solve(board):
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved
    
    row, col = empty
    
    # Try placing numbers 1-9 in the empty spot
    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num
            
            # Recursively solve for the next empty spot
            if solve(board):
                return True
            
            # If placing num doesn't lead to a solution, backtrack
            board[row][col] = 0
    
    return False  # Trigger backtracking if no solution found

# Function to print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Sample Sudoku board (0 represents an empty spot)
sudoku_board = [
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

# Solving the Sudoku puzzle
if solve(sudoku_board):
    print("Solved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists!")
