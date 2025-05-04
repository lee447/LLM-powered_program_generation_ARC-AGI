def solve(grid):
    m = len(grid)
    n = len(grid[0])
    sep_rows = [i for i in range(m) if all(grid[i][j] == grid[i][0] for j in range(n))]
    sep_cols = [j for j in range(n) if all(grid[i][j] == grid[0][j] for i in range(m))]
    sep_color = grid[sep_rows[0]][sep_cols[0]]
    zones = []
    c0 = sep_cols[0]
    zones.append((0, c0-1))
    for a,b in zip(sep_cols, sep_cols[1:]):
        zones.append((a+1, b-1))
    zones.append((sep_cols[-1]+1, n-1))
    bands = []
    r0 = sep_rows[0]
    bands.append((0, r0-1))
    for a,b in zip(sep_rows, sep_rows[1:]):
        bands.append((a+1, b-1))
    bands.append((sep_rows[-1]+1, m-1))
    colors = []
    for rs,re in bands:
        for i in range(rs, re):
            for zs,ze in zones:
                for j in range(zs, ze):
                    c = grid[i][j]
                    if c != sep_color and c != 0:
                        if grid[i][j+1] == c and grid[i+1][j] == c and grid[i+1][j+1] == c:
                            colors.append(c)
    distinct = sorted(set(colors))
    N = len(distinct)
    out = [[0]*N for _ in range(N)]
    for i,c in enumerate(distinct):
        for j in range(i+1):
            out[i][j] = c
    return out