WIN = 100
LOSE = -WIN

evaluation_cache = {}

def scan(disc_set, last_play):
    if disc_set in evaluation_cache:
        return evaluation_cache[disc_set]

    for line in (tuple((last_play[0] + x, last_play[1]) in disc_set for x in range(-3, 4)),
        tuple((last_play[0], last_play[1] + y) in disc_set for y in range(-3, 4)),
        tuple((last_play[0] + a, last_play[1] + a) in disc_set for a in range(-3, 4)),
        tuple((last_play[0] - a, last_play[1] + a) in disc_set for a in range(-3, 4))):
        if sum(line) < 4:
            continue
        for i in range(4):
            if all(line[i:i+4]):
                from utils import print_grid
                evaluation_cache[disc_set] = WIN
                return WIN
    return 0
