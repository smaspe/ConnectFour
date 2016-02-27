import evaluation

from utils import nodes

def minimax(grid, depth, is_max_player, me, op):
    depth -= 1
    if is_max_player:
        best = (evaluation.LOSE, [])
        node = -1
        for i, new_grid in nodes(grid, me):
            current_value = evaluation.scan(new_grid, me ,op)
            if current_value == evaluation.WIN or depth == 0:
                return (current_value, [i])
            v = minimax(new_grid, depth, False, me, op)
            if v[0] > best[0]:
                best = v
                best[1].append(i)
            if best[0] == evaluation.WIN:
                break
        return best
    else:
        best = (evaluation.WIN, [])
        for i, new_grid in nodes(grid, op):
            current_value = evaluation.scan(new_grid, me ,op)
            if current_value == evaluation.LOSE or depth == 0:
                return (current_value, [i])
            v = minimax(new_grid, depth, True, me, op)
            if v[0] < best[0]:
                best = v
                best[1].append(i)
            if best[0] == evaluation.LOSE:
                break
        return best