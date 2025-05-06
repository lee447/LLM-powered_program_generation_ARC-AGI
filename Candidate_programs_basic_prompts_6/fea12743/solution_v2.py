def solve(grid):
    R, C = len(grid), len(grid[0])
    rows = [i for i in range(R) if any(grid[i][j] == 2 for j in range(C))]
    cols = [j for j in range(C) if any(grid[i][j] == 2 for i in range(R))]
    dr = [r for r in range(1, R) if r not in rows]
    dc = [c for c in range(1, C) if c not in cols]
    hr = sorted({i - j for i, j in zip(rows, rows[1:])})
    hc = sorted({i - j for i, j in zip(cols, cols[1:])})
    br = hr[0]
    bc = hc[0]
    out = [row[:] for row in grid]
    for bi in range(len(rows) // br):
        for bj in range(len(cols) // bc):
            r0, c0 = rows[0] + bi * br, cols[0] + bj * bc
            cnt = sum(grid[r0 + i][c0 + j] == 2 for i in range(br) for j in range(bc))
            if cnt == max(cnt for bi2 in range(len(rows) // br) for bj2 in range(len(cols) // bc)
                          for cnt in [sum(grid[rows[0] + bi2*br + i][cols[0] + bj2*bc + j] == 2
                                          for i in range(br) for j in range(bc))]):
                color = 3
            elif cnt > 0:
                color = 8
            else:
                continue
            for i in range(br):
                for j in range(bc):
                    if grid[r0 + i][c0 + j] == 2:
                        out[r0 + i][c0 + j] = color
    return out