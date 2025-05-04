import numpy as np

def solve(grid):
    grid = np.array(grid)
    sep = np.where(grid == 5)[1][0]
    lb = grid[:, :sep]
    rb = grid[:, sep+1:]
    h, w = lb.shape
    out = np.zeros((h, w), int)
    for i in range(h):
        for j in range(w):
            if lb[i, j] != 0:
                out[i, j] = lb[i, j]
            elif rb[i, j] != 0:
                out[i, j] = rb[i, j]
    return out.tolist()