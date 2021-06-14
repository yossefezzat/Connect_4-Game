N, M = 6, 7
n_players = 2
marks = ['X', 'O']

default_grid_cell = '.'


#This function prints the grid of Connect Four Game as the game progresses
def print_grid(grid):
    for i in range(n_players):
        print('Player %d: %c  ' % (i+1, marks[i]), end='')
        if i < n_players-1:
            print('vs  ', end='')
    print()
    print('--' + '---' * M + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(M):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * M + '--')
    return grid

def clear_grid():
    grid = [['.'] * M for i in range(N)]
    return grid
    
#This function checks if given cell is empty or not 
def check_empty(i , grid):
    return grid[0][i] == default_grid_cell

#This function checks if given position is valid or not 
def check_valid_column(i):
    return 0 <= i < M
    
def read_input(grid):
    i = int(input('Enter the column index: '))
    while not check_valid_column(i) or not check_empty(i , grid):
        i = int(input('Enter a valid column index: '))
    return i

def set_cell(i, mark , grid):
    for j in range(N-1, -1, -1):
        if grid[j][i] == default_grid_cell:
            grid[j][i] = mark
            break

def check_left_diagonal(grid):
    for i in range(N-3):
        for j in range(M-3):
            s = {grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3]}
            if grid[i][j] != '.' and len(s) == 1:
                return True
    return False
    
def check_right_diagonal(grid):
    for i in range(N-3):
        for j in range(3, M):
            s = {grid[i][j], grid[i+1][j-1], grid[i+2][j-2], grid[i+3][j-3]}
            if grid[i][j] != '.' and len(s) == 1:
                return True
    return False

def check_rows(grid):
    for i in range(N):
        for j in range(M-3):
            s = {grid[i][j], grid[i][j+1], grid[i][j+2], grid[i][j+3]}
            if grid[i][j] != '.' and len(s) == 1:
                return True
    return False
 
def check_columns(grid):
    for j in range(N-3):
        for i in range(M):
            s = {grid[j][i], grid[j+1][i], grid[j+2][i], grid[j+3][i]}
            if grid[j][i] != '.' and len(s) == 1:
                return True
    return False

#This function checks if the game has a win state or not
def check_win(grid):
    return check_rows(grid) or check_columns(grid) or check_left_diagonal(grid) or check_right_diagonal(grid)

def check_tie():
    pass


