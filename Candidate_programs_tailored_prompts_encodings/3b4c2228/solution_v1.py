from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    zero_rows = [i for i in range(n) if all(grid[i][j] == 0 for j in range(m))]
    zero_cols = [j for j in range(m) if all(grid[i][j] == 0 for i in range(n))]
    hr = [-1] + zero_rows + [n]
    hc = [-1] + zero_cols + [m]
    row_zone = [0]*n
    for zi in range(len(hr)-1):
        for r in range(hr[zi]+1, hr[zi+1]):
            row_zone[r] = zi
    col_zone = [0]*m
    for zj in range(len(hc)-1):
        for c in range(hc[zj]+1, hc[zj+1]):
            col_zone[c] = zj
    found = set()
    for i in range(n-1):
        for j in range(m-1):
            v = grid[i][j]
            if v != 0 and grid[i+1][j] == v and grid[i][j+1] == v and grid[i+1][j+1] == v:
                rz, cz = row_zone[i], col_zone[j]
                found.add((rz, cz))
    out = [[0]*3 for _ in range(3)]
    for d in range(3):
        if (d, d) in found:
            out[d][d] = 1
    return out