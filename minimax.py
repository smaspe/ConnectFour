import evaluation

from utils import nodes

def minimax(grid, depth, is_max_player, me, op):
    depth -= 1
    if is_max_player:
        best = evaluation.LOSE
        for i, new_grid in nodes(grid, me):
            current_value = evaluation.scan(new_grid, me ,op)
            if current_value == evaluation.WIN or depth == 0:
                return current_value
            v = minimax(new_grid, depth, False, me, op)
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
            v = minimax(new_grid, depth, True, me, op)
            best = min(best, v)
            if best == evaluation.LOSE:
                break
        return best
