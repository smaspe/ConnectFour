import evaluation
import utils

grid = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,2,0,0],
    [0,0,0,2,2,0],
    [0,0,1,2,2,2]]

print map(list, utils.diag_grid_gen(list(reversed(grid))))
print map(list, utils.diag_grid_gen(grid))

print evaluation.scan(grid, 1, 2)


grid = [
    [0,1,0,1,1],
    [0,0,0,0,1],
    [2,2,2,2,0],
    [0,0,0,0,1],
    [0,0,0,0,0]]

print evaluation.scan(grid, 1, 2)

grid = [
    [1,1,0,1,1],
    [0,0,0,0,1],
    [0,0,0,0,0],
    [0,0,0,0,1],
    [0,0,0,0,0]]

print evaluation.scan(grid, 2, 1)

grid = [
    [0,0,0,0,1],
    [0,0,0,1,1],
    [0,0,1,0,1],
    [0,0,0,0,0],
    [0,0,0,0,1]]

print evaluation.scan(grid, 1, 2)

grid = [
    [0,0,0,0,1,0],
    [0,0,0,1,1,0],
    [0,0,1,0,0,0],
    [0,1,0,0,0,0],
    [0,0,0,0,1,0]]

print evaluation.scan(grid, 1, 2)

grid = [[1,0,1,1,1,1]]
print evaluation.scan(grid, 1, 2)
