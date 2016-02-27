import sys
from utils import nodes
from minimax import minimax

settings = {}
current_grid = [[0]]
current_round = 0

current_depth = 4

def select_move(grid, time, settings):
    global current_depth
    if time == settings['timebank']:
        current_depth += 1
    elif time == settings['time_per_move']:
        current_depth = 3
    elif time < settings['timebank'] / 2 and current_depth > 3:
        current_depth -= 1
    me = settings['your_botid']
    # assuming the ids are always 1 and 2?
    op = [2,1][me - 1]

    values = minimax(grid, current_depth, True, me, op)
    if values and values[1]:
        return values[1][-1]
    # Nothing of worth was found (we probably lost)
    return next(nodes(grid, me))[0]

if __name__ == '__main__':
    while True:
        line = raw_input()
        if not line:
            continue
        content = line.split()
        if content[0] == 'settings':
            try:
                settings[content[1]] = int(content[2])
            except:
                settings[content[1]] = content[2]
            if content[1] == 'your_botid':
                me = int(content[2])
                # assuming the ids are always 1 and 2?
                op = [2,1][me - 1]
        elif content[0] == 'update':
            if content[2] == 'field':
                current_grid = [[int(x) for x in y.split(',')] for y in content[3].split(';')]
            elif content[2] == 'round':
                current_round = int(content[3])
        elif content[0] == 'action':
            if current_round == 1:
                sys.stdout.write(('place_disc %d' % (settings['field_columns'] // 2)) + '\n')
                sys.stdout.flush()
                continue
            time = int(content[2])
            sys.stdout.write(('place_disc %d' % select_move(current_grid, time, settings)) + '\n')
            sys.stdout.flush()
