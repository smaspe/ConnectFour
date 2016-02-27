from utils import window, diag_grid_gen

EMPTY = 0
WIN = 100
LOSE = -WIN

# TODO for better choosing, count only distinct empty cells as threes
# TODO also count 0 1 1 1 0 as 2
def generic_scan(gen, color):
    threes = 0
    for row in gen:
        for seq in window(row, 4):
            cnt = seq.count(color)
            if cnt == 4:
                return WIN
            if cnt == 3 and seq.count(EMPTY) == 1:
                threes += 1
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
    return generic_scan(diag_grid_gen(grid), color)

def scan(grid, me, op):
    inverted_grid = zip(*grid)
    reversed_grid = list(reversed(grid))

    three_count = 0
    # Opponent first
    for res in (linear_scan(grid, op), linear_scan(inverted_grid, op), diag_scan(grid, op), diag_scan(reversed_grid, op)):
        if res == WIN:
            return LOSE
        three_count -= res

    # Then me
    for res in (linear_scan(grid, me), linear_scan(inverted_grid, me), diag_scan(grid, me), diag_scan(reversed_grid, me)):
        if res == WIN:
            return WIN
        # three_count += res

    return three_count
