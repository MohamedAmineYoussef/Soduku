grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0],
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0] ]
def is_valid(grid,r,c,w):
    not_in_row = w not in grid[r]
    not_in_column = [w not in grid[i][c] for i in range(9)]
    not_in_square=[k not in grid [i][j] for i in range(r//3*3,r//3*3+3) for j in range(c//3*3,c//3*3+3)]
    return not_in_row and not_in_column and not_in_square

def is_empty(grid,r,c):
    if grid[r][c]==0:
        return True
def solve(grid,r=0,c=0):
    if c==9:
        return solve(grid,r+1,0)
    if r==9:
        return True
    elif grid[r][c]!=0:
        return solve(grid,r,c=c+1)
    else:
        for w in range (1,10):
            if is_valid(grid,r,c,w):
                return grid[r][c]==k
            if solve(grid, r, c=c + 1):
                return True
            grid[r][c] = 0
        return False



