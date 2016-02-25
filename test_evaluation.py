import evaluation

grid = [
    [0,0,0,0,1],
    [0,0,0,0,1],
    [0,0,0,0,0],
    [0,0,0,0,1],
    [0,0,0,0,0]]

print evaluation.scan(grid, 1)


grid = [
    [0,1,0,1,1],
    [0,0,0,0,1],
    [0,0,0,0,0],
    [0,0,0,0,1],
    [0,0,0,0,0]]

print evaluation.scan(grid, 1)

grid = [
    [1,1,0,1,1],
    [0,0,0,0,1],
    [0,0,0,0,0],
    [0,0,0,0,1],
    [0,0,0,0,0]]

print evaluation.scan(grid, 1)

grid = [
    [0,0,0,0,1],
    [0,0,0,1,1],
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,0,1]]

print evaluation.scan(grid, 1)

grid = [
    [0,0,0,0,1],
    [0,0,0,1,1],
    [0,0,1,0,0],
    [0,1,0,0,0],
    [0,0,0,0,1]]

print evaluation.scan(grid, 1)
