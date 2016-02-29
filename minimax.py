import evaluation

from utils import nodes

def minimax(my_discs, op_discs, depth, is_max_player, cols, rows):
    if is_max_player:
        best = (evaluation.LOSE - 1, [])
        node = -1
        for disc, new_discs in nodes(my_discs, op_discs, cols, rows):
            current_value = evaluation.scan(new_discs, disc)
            if current_value == evaluation.WIN or depth == 0:
                return (current_value, [disc])
            v = minimax(new_discs, op_discs, depth - 1, False, cols, rows)
            if v[0] > best[0]:
                best = v
                best[1].append(disc)
            if best[0] == evaluation.WIN:
                break
        if best[0] == evaluation.LOSE - 1:
            # no move to play, draw
            best = (0, [])
        return best
    else:
        best = (evaluation.WIN + 1, [])
        for disc, new_discs in nodes(op_discs, my_discs, cols, rows):
            current_value = evaluation.scan(new_discs, disc)
            if current_value == evaluation.WIN or depth == 0:
                current_value = -current_value
                return (current_value, [disc])
            v = minimax(my_discs, new_discs, depth - 1, True, cols, rows)
            if v[0] < best[0]:
                best = v
                best[1].append(disc)
                # No early escape to capture shorter paths.
#            if best[0] == evaluation.LOSE:
#                break

        if best[0] == evaluation.WIN + 1:
            # no move to play, draw
            best = (0, [])
        return best
