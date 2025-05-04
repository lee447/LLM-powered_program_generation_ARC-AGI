from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0]) if grid else (0, 0)
    runs = {}
    for i in range(h):
        prev, length = 0, 0
        for j in range(w):
            c = grid[i][j]
            if c != 0 and c == prev:
                length += 1
            else:
                if prev != 0:
                    runs[prev] = max(runs.get(prev, 0), length)
                prev, length = c, 1 if c != 0 else 0
        if prev != 0:
            runs[prev] = max(runs.get(prev, 0), length)
    for j in range(w):
        prev, length = 0, 0
        for i in range(h):
            c = grid[i][j]
            if c != 0 and c == prev:
                length += 1
            else:
                if prev != 0:
                    runs[prev] = max(runs.get(prev, 0), length)
                prev, length = c, 1 if c != 0 else 0
        if prev != 0:
            runs[prev] = max(runs.get(prev, 0), length)
    sorted_runs = sorted(((l,c) for c,l in runs.items()), reverse=True)
    if not sorted_runs:
        return []
    m = sorted_runs[0][0]
    out = [[0]*m for _ in range(m)]
    for k,(_,col) in enumerate(sorted_runs):
        o, e = k, m-1-k
        for x in range(o, e+1):
            out[o][x] = col
            out[e][x] = col
            out[x][o] = col
            out[x][e] = col
    return out