from itertools import islice

def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def diag_grid_gen(grid):
    def diag_row_gen(x, y, max_x):
        while x < max_x and y >= 0:
            cell = grid[y][x]
            yield cell
            y -= 1
            x += 1
    for i in range(3, len(grid) + len(grid[0]) - 4):
        if i >= len(grid):
            y = len(grid) - 1
        else:
            y = i
        x = i - y
        yield diag_row_gen(x, y, len(grid[0]))

def play(grid, column, color):
    grid = [x[:] for x in grid]
    for row in reversed(grid):
        if row[column] == 0:
            row[column] = color
            return grid
    # Can't play there
    return None

def nodes(grid, player):
    l = len(grid[0])
    for i in sorted(range(l), key=lambda x: abs(x - l // 2)):
        new_grid = play(grid, i, player)
        if new_grid:
            yield i, new_grid
