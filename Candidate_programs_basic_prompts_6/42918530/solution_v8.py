def solve(grid):
    H, W = len(grid), len(grid[0])
    row_seps = [i for i in range(H) if all(cell == 0 for cell in grid[i])]
    col_seps = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    rows = [(row_seps[i]+1, row_seps[i+1]-1) for i in range(len(row_seps)-1)]
    cols = [(col_seps[j]+1, col_seps[j+1]-1) for j in range(len(col_seps)-1)]
    out = [list(r) for r in grid]
    for r0, r1 in rows:
        for c0, c1 in cols:
            c = grid[r0][c0]
            if c == 0: continue
            hollow = True
            for i in range(r0, r1+1):
                for j in range(c0, c1+1):
                    if i in (r0, r1) or j in (c0, c1):
                        if grid[i][j] != c: hollow = False
                    else:
                        if grid[i][j] != 0: hollow = False
            if hollow:
                ci = (r0 + r1) // 2
                cj = (c0 + c1) // 2
                for j in range(c0+1, c1):
                    out[ci][j] = c
                for i in range(r0+1, r1):
                    out[i][cj] = c
    return out