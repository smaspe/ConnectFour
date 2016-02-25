EMPTY = 0
WIN = 100

def linear_scan(grid, color):
    three_count = 0
    for row in grid:
        color_count = 0
        three = False
        for cell in row:
            if cell == color:
                color_count += 1
            else if cell == EMPTY:
                three = True
            else:
                color_count = 0
                three = False
            if color_count == 4:
                return WIN
            if color_count == 3 and three:
                three_count += 1
    return three_count

def diag_scan(grid, color):
    three_count = 0
    for i in range(4, len(grid) + len(grid[0]) - 4):
        if i >= len(grid):
            y = len(grid) - 1
        else:
            y = i
        x = i - y
        color_count = 0
        three = False
        while x < len(grid[0]) and y > 0:
            cell = grid[x][y]
            if cell == color:
                color_count += 1
            else if cell == EMPTY:
                three = True
            else:
                color_count = 0
                three = False
            if color_count == 4:
                return WIN
            if color_count == 3 and three:
                three_count += 1
            y -= 1
            x += 1
    return three_count


def scan(grid, color):
    inverted_grid = zip(*grid)
    # scan horizontally
    three_count = 0
    res = linear_scan(grid, color)
    if res == WIN:
        return WIN
    three_count += res

    # scan vertically
    res = linear_scan(inverted_grid, color)
    if res == WIN:
        return WIN
    three_count += res

    # scan diagonally
    res = diag_scan(grid, color)
    if res == WIN:
        return WIN
    three_count += res

    # scan diagonally (the other one)
    res = diag_scan(inverted_grid, color)
    if res == WIN:
        return WIN
    three_count += res

    return three_count
