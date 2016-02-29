from minimax import minimax
import utils

value = '''0|0|0|0|0|0|0
0|0|0|2|2|0|0
0|0|0|2|1|2|0
0|0|0|1|1|1|0
0|0|1|1|2|2|0
0|0|1|1|2|2|0'''
grid = [[int(x) for x in y.split('|')] for y in value.split('\n')]
my_discs, op_discs = utils.grid_as_set(grid, 1, 2)

my_discs |= set([1, 5])


print minimax(my_discs, op_discs, 1, True, 6, 7)
