from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    sep_rows = [i for i in range(m) if all(grid[i][j] == grid[i][0] for j in range(n))]
    sep_cols = [j for j in range(n) if all(grid[i][j] == grid[0][j] for i in range(m))]
    sep_color = grid[sep_rows[0]][sep_cols[0]]
    bands = []
    prev = -1
    for r in sep_rows:
        if r - prev - 1 >= 2:
            bands.append((prev+1, r-1))
        prev = r
    if m - prev - 1 >= 2:
        bands.append((prev+1, m-1))
    zones = []
    prev = -1
    for c in sep_cols:
        if c - prev - 1 >= 2:
            zones.append((prev+1, c-1))
        prev = c
    if n - prev - 1 >= 2:
        zones.append((prev+1, n-1))
    colors = set()
    for rs, re in bands:
        for zs, ze in zones:
            for i in range(rs, re):
                for j in range(zs, ze):
                    c = grid[i][j]
                    if c != 0 and c != sep_color:
                        if grid[i][j+1] == c and grid[i+1][j] == c and grid[i+1][j+1] == c:
                            colors.add(c)
    distinct = sorted(colors)
    N, M = len(distinct), len(zones)
    out = [[0]*M for _ in range(N)]
    for i, c in enumerate(distinct):
        for j in range(i+1):
            out[i][j] = c
    return out