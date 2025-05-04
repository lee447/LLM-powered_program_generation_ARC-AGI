from collections import Counter
def solve(grid):
    H, W = len(grid), len(grid[0])
    sep = []
    for r,row in enumerate(grid):
        mc = Counter(row).most_common(1)[0]
        if mc[1] >= W-1:
            sep.append(r)
    if len(sep) < 2:
        return grid
    L = sep[1] - sep[0] - 1
    patterns = []
    segments = len(sep) - 1
    for i in range(L):
        cols = []
        for j in range(segments):
            r = sep[j] + 1 + i
            cols.append(grid[r])
        proto = []
        for c in range(W):
            vals = [row[c] for row in cols]
            proto.append(Counter(vals).most_common(1)[0][0])
        patterns.append(proto)
    out = [row[:] for row in grid]
    for j in range(segments):
        for i in range(L):
            out[sep[j] + 1 + i] = patterns[i][:]
    for r in sep:
        out[r] = [Counter(grid[r]).most_common(1)[0][0]] * W
    return out