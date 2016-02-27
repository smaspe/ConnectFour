EMPTY = 0
WIN = 100
LOSE = -WIN

# TODO for better choosing, count only distinct empty cells as threes
# TODO also count 0 1 1 1 0 as 2
def generic_scan(gen, color):
    threes = 0
    for row in gen:
        four_count = 0
        three_count = 0
        three = False
        for cell in row:
            if cell == color:
                four_count += 1
                three_count += 1
            elif cell == EMPTY:
                three = True
                four_count = 0
            else:
                four_count = 0
                three_count = 0
                three = False
            if four_count == 4:
                return WIN
            if three_count == 3 and three:
                threes += 1
                three_count = 0
                three = False
    return threes

def linear_scan(grid, color):
    def grid_gen(grid):
        def row_gen(row):
            for cell in row:
                yield cell
        for row in grid:
            yield row_gen(row)
    return generic_scan(grid_gen(grid), color)

def diag_scan(grid, color):
    def grid_gen(grid):
        def row_gen(x, y, max_x):
            while x < max_x and y > 0:
                cell = grid[y][x]
                yield cell
                y -= 1
                x += 1
        for i in range(4, len(grid) + len(grid[0]) - 4):
            if i >= len(grid):
                y = len(grid) - 1
            else:
                y = i
            x = i - y
            yield row_gen(x, y, len(grid[0]))
    return generic_scan(grid_gen(grid), color)

def scan(grid, me, op):
    inverted_grid = zip(*grid)

    three_count = 0
    # Opponent first
    for f in (linear_scan, diag_scan):
        for g in (grid, inverted_grid):
            res = f(g, op)
            if res == WIN:
                return LOSE
            three_count -= res

    # Then me
    for f in (linear_scan, diag_scan):
        for g in (grid, inverted_grid):
            res = f(g, me)
            if res == WIN:
                return WIN
            # three_count += res

    return three_count
