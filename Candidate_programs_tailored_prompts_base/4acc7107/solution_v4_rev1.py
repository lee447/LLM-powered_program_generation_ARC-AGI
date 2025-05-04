from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    colors = sorted({v for row in grid for v in row if v != 0})
    square_pos = {}
    orient = {}
    for c in colors:
        for i in range(n-1):
            for j in range(m-1):
                if grid[i][j]==c and grid[i+1][j]==c and grid[i][j+1]==c and grid[i+1][j+1]==c:
                    square_pos[c] = (i, j)
                    break
            if c in square_pos: break
        found = False
        for i in range(n):
            for j in range(m-3):
                if all(grid[i][j+k]==c for k in range(4)):
                    orient[c] = 'H'
                    found = True
                    break
            if found: break
        if not found:
            for i in range(n-3):
                for j in range(m):
                    if all(grid[i+k][j]==c for k in range(4)):
                        orient[c] = 'V'
                        found = True
                        break
                if found: break
    order = sorted(colors, key=lambda c: square_pos[c][0])
    h_s, w_s = 2, 2
    bh = {}
    bw = {}
    for c in colors:
        if orient[c] == 'H':
            bh[c], bw[c] = 1, 4
        else:
            bh[c], bw[c] = 4, 1
    ah = {c: max(h_s, bh[c]) for c in colors}
    aw = {c: max(w_s, bw[c]) for c in colors}
    total_w = sum(aw[c] for c in order) + (len(order) - 1)
    block_h = max(ah[c] for c in colors)
    start_row = n - block_h
    out = [[0]*m for _ in range(n)]
    cur_col = 0
    for c in order:
        r0 = start_row + (block_h - ah[c])
        c0 = cur_col
        for dr in (0,1):
            for dc in (0,1):
                out[r0+dr][c0+dc] = c
        i0, j0 = r0+1, c0+1
        if orient[c] == 'H':
            for k in range(4):
                out[i0][j0+k] = c
        else:
            for k in range(4):
                out[i0+k][j0] = c
        cur_col += aw[c] + 1
    return out