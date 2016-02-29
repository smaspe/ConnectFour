import sys
import utils
from minimax import minimax
import evaluation

log = False
settings = {}
current_round = 0
my_discs = set()
op_discs = set()
op_move = ()

depth = 4

def select_move(my_discs, op_discs, op_move, time, settings):
    global current_depth
    if time == settings['timebank']:
        depth += 1
    elif time == settings['time_per_move']:
        depth = 4
    elif time < settings['timebank'] / 2 and current_depth > 4:
        depth -= 1
    me = settings['your_botid']
    # assuming the ids are always 1 and 2?
    op = [2,1][me - 1]

    moves = []
    for disc, new_discs in utils.nodes(my_discs, op_discs, settings['field_columns'], settings['field_rows']):
        current_value = evaluation.scan(new_discs, disc)
        if current_value == evaluation.WIN:
            moves.append((current_value, [disc]))
            break
        move = minimax(new_discs, op_discs, depth - 1, False, settings['field_columns'], settings['field_rows'])
        move[1].append(disc)
        moves.append(move)
    moves.sort(key=lambda move: -len(move[1]))
    moves.sort(key=lambda move: -move[0])
    if not moves or not moves[0] or not moves[0][1]:
        # Nothing of worth was found (we probably lost)
        return next(utils.nodes(my_discs, op_discs))[0][0]
    move = moves[0]
    if log:
        print 'minimax result', move
        for _move in moves:
            print _move

    if move[0] == evaluation.LOSE:
        # All moves are losing, take the one that takes the longest
        moves.sort(key=lambda move: -len(move[1]))
        move = moves[0]

    if move[0] == 0:
        # not losing, but no winning move found, playing close to center
        moves = [mv[-1] for score, mv in moves if score != evaluation.LOSE]
        moves.sort(key=lambda (x, y): abs(x - settings['field_columns'] // 2) - y)
        if log:
            print moves
        return moves[0][0]
    else:
        return move[1][-1][0]

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
                my_discs, new_op_discs = utils.parse_grid(content[3], me, op)
                op_move = next(iter(new_op_discs - op_discs), None)
                op_discs = new_op_discs
            elif content[2] == 'round':
                current_round = int(content[3])
        elif content[0] == 'action':
            if current_round == 1:
                sys.stdout.write(('place_disc %d' % (settings['field_columns'] // 2)) + '\n')
                sys.stdout.flush()
                continue
            time = int(content[2])
            sys.stdout.write(('place_disc %d' % select_move(my_discs, op_discs, op_move, time, settings)) + '\n')
            sys.stdout.flush()
