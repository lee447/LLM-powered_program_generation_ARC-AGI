import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    arr = np.array(grid)
    vals, cnts = np.unique(arr, return_counts=True)
    bg = vals[np.argmax(cnts)]
    t = vals[vals != bg][0]
    max_run = []
    for r in range(h):
        row = arr[r] == t
        runs = np.diff(np.concatenate(([0], row.view(np.int8), [0])))
        starts = np.where(runs == 1)[0]
        ends = np.where(runs == -1)[0] - 1
        max_run.append(ends - starts + 1 if len(starts) else [0])
    H = int(np.argmax([max(sr) if isinstance(sr, np.ndarray) or isinstance(sr, list) else sr for sr in max_run]))
    stripe_cols = []
    for c in range(w):
        col = arr[:, c]
        above = np.sum(col[:H] == t)
        below = np.sum(col[H+1:] == t)
        if above > 0 and below > 0:
            stripe_cols.append(c)
    out = np.full((h, w), bg, int)
    for r in range(h):
        if r == H:
            out[r, arr[r] == t] = t
        else:
            for c in stripe_cols:
                if arr[r, c] == t:
                    out[r, c] = t
    return out.tolist()