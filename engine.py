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

grid = [[0 for _ in range(7)] for _ in range(6)]

#value = '0,0,0,0,0,0,1;0,0,0,2,0,0,1;0,2,0,1,0,2,1;0,2,0,2,0,1,2;0,1,1,2,0,2,1;0,2,2,1,1,2,1'
#grid = [[int(x) for x in y.split(',')] for y in value.split(';')]

for i in range(2, 22):
    print 'Round %d' % i
    bot_p.stdin.write('update game round %d\n' % i)
    bot_p.stdin.write('update game field %s\n' % (';'.join(','.join(str(cell) for cell in row) for row in grid)))
    bot_p.stdin.write('action move 500\n')

    cmd = [None]
    while cmd[0] != 'place_disc':
        cmd = bot_p.stdout.readline()
        print cmd
        cmd = cmd.split()

    column = int(cmd[1])
    grid = utils.play(grid, column, 1)

    print '\n'.join('|'.join(str(cell) for cell in row) for row in grid)

    new_grid = None
    while not new_grid:
        column = int(raw_input('Your move (0-6) '))
        new_grid = utils.play(grid, column, 2)
    grid = new_grid
    print '\n'.join('|'.join(str(cell) for cell in row) for row in grid)
