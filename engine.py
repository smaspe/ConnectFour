from subprocess import Popen, PIPE

import utils

bot_p = Popen(['python', 'bot.py'], stdin=PIPE, stdout=PIPE, bufsize=1)

init = ['settings timebank 10000',
    'settings time_per_move 500',
    'settings player_names player1,player2',
    'settings your_bot player1',
    'settings your_botid 1',
    'settings field_columns 7',
    'settings field_rows 6']

for l in init:
    bot_p.stdin.write(l + '\n')

#value = '0,0,0,0,0,0,1;0,0,0,2,0,0,1;0,2,0,1,0,2,1;0,2,0,2,0,1,2;0,1,1,2,0,2,1;0,2,2,1,1,2,1'
#grid = [[int(x) for x in y.split(',')] for y in value.split(';')]
value = '''
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 2 | 0 | 0 |
'''
value = '''
| 1 | 0 | 1 | 2 | 0 | 0 | 2 |
| 1 | 1 | 2 | 1 | 1 | 0 | 2 |
| 2 | 2 | 2 | 1 | 2 | 2 | 1 |
| 1 | 1 | 2 | 2 | 2 | 1 | 2 |
| 1 | 2 | 1 | 1 | 2 | 2 | 2 |
| 1 | 1 | 2 | 1 | 1 | 1 | 2 |
'''
grid = [[int(x.strip()) for x in y.split('|') if x.strip()] for y in value.strip().split('\n')]
my_discs, op_discs = utils.grid_as_set(grid, 1, 2)

#my_discs, op_discs = set(), set()

for i in range(2, 22):
    print 'Round %d' % i
    bot_p.stdin.write('update game round %d\n' % i)
    bot_p.stdin.write('update game field %s\n' % (';'.join(','.join(str(cell) for cell in row) for row in utils.engine_grid(my_discs, op_discs))))
    bot_p.stdin.write('action move 500\n')

    cmd = [None]
    while cmd[0] != 'place_disc':
        cmd = bot_p.stdout.readline()
        print cmd
        cmd = cmd.split()

    column = int(cmd[1])
    my_discs |= set([(column, min([y for (x, y) in my_discs | op_discs if x == column] + [6]) - 1)])
    utils.print_grid(my_discs, op_discs)

    y = -1
    while y < 0:
        column = int(raw_input('Your move (0-6) '))
        y = min([y for (x, y) in my_discs | op_discs if x == column] + [6]) - 1
    op_discs |= set([(column, y)])

    utils.print_grid(my_discs, op_discs)
