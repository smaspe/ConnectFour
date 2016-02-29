from itertools import islice

def grid_as_set(grid, me, op):
    my_discs = frozenset((x, y) for y, row in enumerate(grid) for x, value in enumerate(row) if value == me)
    op_discs = frozenset((x, y) for y, row in enumerate(grid) for x, value in enumerate(row) if value == op)
    return (my_discs, op_discs)

def parse_grid(grid_as_string, me, op):
    grid = [[int(x) for x in y.split(',')] for y in grid_as_string.split(';')]
    return grid_as_set(grid, me, op)

def nodes(current_discs, other_discs, cols, rows):
    for move in moves(current_discs, other_discs, cols, rows):
        yield (move, current_discs | set([move]))

def moves(current_discs, other_discs, cols, rows):
    for x in range(cols):
        for y in range(rows-1, -1, -1):
            if (x, y) not in other_discs and (x, y) not in current_discs:
                yield (x, y)
                break

def print_grid(my_discs, op_discs):
    print '+---' * 7 + '+'
    for y in range(6):
        print '|',
        for x in range(7):
            if (x, y) in my_discs:
                print 1,'|',
            elif (x, y) in op_discs:
                print 2,'|',
            else:
                print 0,'|',
        print '\n',
        print '+---' * 7 + '+'

def engine_grid(my_discs, op_discs):
    grid = []
    for y in range(6):
        row = []
        for x in range(7):
            if (x, y) in my_discs:
                row.append(1)
            elif (x, y) in op_discs:
                row.append(2)
            else:
                row.append(0)
        grid.append(row)
    return grid
