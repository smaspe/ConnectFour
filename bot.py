import evaluation
import sys

settings = {}
current_grid = [[0]]
current_round = 0
me = -1
op = -1
current_depth = 4

def play(grid, column, color):
    grid = [x[:] for x in grid]
    for row in reversed(grid):
        if row[column] == 0:
            row[column] = color
            return grid
    # Can't play there
    return None

def nodes(grid, player):
    for i in range(settings['field_columns']):
        new_grid = play(grid, i, player)
        if new_grid:
            yield i, new_grid

def minimax(grid, depth, is_max_player):
    depth -= 1
    if is_max_player:
        best = evaluation.LOSE
        for i, new_grid in nodes(grid, me):
            current_value = evaluation.scan(new_grid, me ,op)
            if current_value == evaluation.WIN or depth == 0:
                return current_value
            v = minimax(new_grid, depth, False)
            best = max(best, v)
            if best == evaluation.WIN:
                break
        return best
    else:
        best = evaluation.WIN
        for i, new_grid in nodes(grid, op):
            current_value = evaluation.scan(new_grid, me ,op)
            if current_value == evaluation.LOSE or depth == 0:
                return current_value
            v = minimax(new_grid, depth, True)
            best = min(best, v)
            if best == evaluation.LOSE:
                break
        return best

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
            if time == settings['timebank']:
                current_depth += 1
            elif time < settings['timebank'] / 2:
                current_depth -= 2
            values = sorted((minimax(g, current_depth, False), i) for i, g in nodes(current_grid, me))
            sys.stdout.write(('place_disc %d' % values[-1][1]) + '\n')
            sys.stdout.flush()
            # TODO get the remaining time?
            # TODO get the per-turn time?
