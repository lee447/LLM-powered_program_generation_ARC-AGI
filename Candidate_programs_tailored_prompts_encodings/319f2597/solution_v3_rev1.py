import numpy as np
def solve(grid):
    arr = np.array(grid)
    h, w = arr.shape
    blank_rows = [i for i in range(h) if (arr[i] == 0).all()]
    blank_cols = [j for j in range(w) if (arr[:, j] == 0).all()]
    if blank_rows and blank_cols:
        for i in blank_rows:
            arr[i, :] = 0
        for j in blank_cols:
            arr[:, j] = 0
    elif blank_rows:
        k = len(blank_rows)
        start = (w - k) // 2
        for j in range(start, start + k):
            arr[:, j] = 0
    elif blank_cols:
        k = len(blank_cols)
        start = (h - k) // 2
        for i in range(start, start + k):
            arr[i, :] = 0
    return arr.tolist()