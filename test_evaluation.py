import evaluation

grid = [
    [0,0,0,0,1],
    [0,0,0,0,1],
    [0,0,0,0,0],
    [0,0,0,0,1],
    [0,0,0,0,0]]

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

print evaluation.scan(grid, 1, 2)

grid = [
    [0,0,0,0,1],
    [0,0,0,1,1],
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,0,1]]

print evaluation.scan(grid, 1, 2)

grid = [
    [0,0,0,0,1],
    [0,0,0,1,1],
    [0,0,1,0,0],
    [0,1,0,0,0],
    [0,0,0,0,1]]

print evaluation.scan(grid, 1, 2)

grid = [[1,0,1,1,1,1]]
print evaluation.scan(grid, 1, 2)
