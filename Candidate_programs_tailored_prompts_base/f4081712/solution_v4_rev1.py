import numpy as np

def solve(grid):
    arr = np.array(grid)
    n, m = arr.shape

    # find the "divider" color: the color that forms the longest straight horizontal or vertical stripe
    best_color = None
    best_len = -1
    orientation = None
    pos = None
    # horizontal stripes
    for i in range(n):
        row = arr[i]
        for color in np.unique(row):
            if color == 0: continue
            runs = np.diff(np.where(np.concatenate(([True], row[:-1]!=row[1:], [True])))[0])
            # compute run lengths for this color
            mask = (row == color).astype(int)
            lengths = np.diff(np.where(np.concatenate(([0], mask, [0])))[0]) - 1
            mx = lengths.max() if lengths.size>0 else 0
            if mx > best_len:
                best_len = mx
                best_color = color
                orientation = 'H'
                pos = (i, int(np.where(mask.reshape(-1,1).max(axis=0))[0]))
    # vertical stripes
    for j in range(m):
        col = arr[:,j]
        for color in np.unique(col):
            if color == 0: continue
            mask = (col == color).astype(int)
            lengths = np.diff(np.where(np.concatenate(([0], mask, [0])))[0]) - 1
            mx = lengths.max() if lengths.size>0 else 0
            if mx > best_len:
                best_len = mx
                best_color = color
                orientation = 'V'
                pos = (int(np.where(mask.reshape(1,-1).max(axis=1))[0]), j)

    # locate the stripe fully
    if orientation == 'H':
        i = pos[0]
        mask = (arr[i] == best_color)
        runs = np.where(mask)[0]
        start, end = runs[0], runs[-1]
        h, w = end-start+1, end-start+1  # square side = stripe length
        # choose the block above or below
        if i*2 < n:
            si = i + 1
        else:
            si = i - h
        sj = start
    else:
        j = pos[1]
        mask = (arr[:,j] == best_color)
        runs = np.where(mask)[0]
        start, end = runs[0], runs[-1]
        h, w = end-start+1, end-start+1
        if j*2 < m:
            sj = j + 1
        else:
            sj = j - w
        si = start

    sub = arr[si:si+h, sj:sj+w]
    return sub.tolist()