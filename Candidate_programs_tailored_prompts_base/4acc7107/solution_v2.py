def solve(grid):
    n, m = len(grid), len(grid[0])
    colors = sorted({grid[i][j] for i in range(n) for j in range(m) if grid[i][j] != 0})
    square_pos = {}
    bar_pos = {}
    orient = {}
    for c in colors:
        for i in range(n - 1):
            for j in range(m - 1):
                if grid[i][j] == c and grid[i+1][j] == c and grid[i][j+1] == c and grid[i+1][j+1] == c:
                    square_pos[c] = (i, j)
                    break
            if c in square_pos: break
        found = False
        for i in range(n):
            for j in range(m - 3):
                if all(grid[i][j+k] == c for k in range(4)):
                    bar_pos[c] = (i, j)
                    orient[c] = 'H'
                    found = True
                    break
            if found: break
        if not found:
            for i in range(n - 3):
                for j in range(m):
                    if all(grid[i+k][j] == c for k in range(4)):
                        bar_pos[c] = (i, j)
                        orient[c] = 'V'
                        found = True
                        break
                if found: break
    sq_row = {c: square_pos[c][0] for c in colors}
    order = sorted(colors, key=lambda c: sq_row[c])
    h_s, w_s = 2, 2
    bh = {}
    bw = {}
    for c in colors:
        if orient[c] == 'H':
            bh[c], bw[c] = 1, 4
        else:
            bh[c], bw[c] = 4, 1
    ah = {c: max(h_s, bh[c]) for c in colors}
    total_h = sum(ah[c] for c in order) + (len(order)-1)
    start_row = n - total_h
    tops = {}
    cur = start_row
    for i, c in enumerate(order):
        tops[c] = cur
        cur += ah[c] + 1
    out = [[0]*m for _ in range(n)]
    for c in colors:
        r0, c0 = tops[c], 0
        for dr, dc in ((0,0),(0,1),(1,0),(1,1)):
            out[r0+dr][c0+dc] = c
        if orient[c] == 'H':
            for k in range(4):
                out[r0][c0+2+k] = c
        else:
            for k in range(4):
                out[r0+k][c0+2] = c
    return out