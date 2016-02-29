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
    global depth
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
    value = evaluation.LOSE
    for disc, new_discs in utils.nodes(my_discs, op_discs, settings['field_columns'], settings['field_rows']):
        current_value = evaluation.scan(new_discs, disc)
        if current_value == evaluation.WIN:
            moves = [(current_value, [disc])]
            break
        move = minimax(new_discs, op_discs, depth - 1, False, settings['field_columns'], settings['field_rows'])
        move[1].append(disc)
        moves.append(move)
    if not moves or not moves[0] or not moves[0][1]:
        # No valid move found
        return 0
    if log:
        print 'minimax result'
        for _move in moves:
            print _move

    value = max(move[0] for move in moves)
    moves = filter(lambda move: move[0] == value, moves)

    if value == evaluation.LOSE:
        # Those moves are losing, take the one that takes the longest
        moves.sort(key=lambda move: -len(move[1]))
    elif value == evaluation.WIN:
        # Those moves are winning, take the shortest
        moves.sort(key=lambda move: len(move[1]))
    elif value == 0:
        # not losing, but no winning move found, playing close to center
        moves.sort(key=lambda move: abs(move[1][-1][0] - settings['field_columns'] // 2) - move[1][-1][1])

    move = moves[0]
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
