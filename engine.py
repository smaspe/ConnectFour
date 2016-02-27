from subprocess import Popen, PIPE

import bot

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

for i in range(1, 22):
    print 'Round %d' % i
    bot_p.stdin.write('update game round %d\n' % i)
    bot_p.stdin.write('update game field %s\n' % (';'.join(','.join(str(cell) for cell in row) for row in grid)))
    bot_p.stdin.write('action move 10000\n')

    cmd = bot_p.stdout.readline()
    column = int(cmd.split()[1])
    grid = bot.play(grid, column, 1)

    print '\n'.join('|'.join(str(cell) for cell in row) for row in grid)

    new_grid = None
    while not new_grid:
        column = int(raw_input('Your move (0-6) '))
        new_grid = bot.play(grid, column, 2)
    grid = new_grid
    print '\n'.join('|'.join(str(cell) for cell in row) for row in grid)
