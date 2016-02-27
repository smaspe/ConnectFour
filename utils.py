
def play(grid, column, color):
    grid = [x[:] for x in grid]
    for row in reversed(grid):
        if row[column] == 0:
            row[column] = color
            return grid
    # Can't play there
    return None

def nodes(grid, player):
    for i in range(len(grid[0])):
        new_grid = play(grid, i, player)
        if new_grid:
            yield i, new_grid
