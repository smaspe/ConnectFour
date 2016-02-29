import utils

value = '0,0,0,0,0,0,1;0,0,0,2,0,0,1;0,2,0,1,0,2,1;0,2,0,2,0,1,2;0,1,1,2,0,2,1;0,2,2,1,1,2,1'
my_discs, op_discs = utils.parse_grid(value, 1, 2)
print my_discs
print op_discs

utils.print_grid(my_discs, op_discs)

print list(utils.nodes(my_discs, op_discs, 6, 7))
