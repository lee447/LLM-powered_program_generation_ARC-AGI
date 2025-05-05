def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 2:
                ar, ac = r, c
                break
        else:
            continue
        break
    bars = []
    for r in range(h):
        for c in range(w):
            col = grid[r][c]
            if col in (1, 3):
                if c + 2 < w and grid[r][c+1] == col and grid[r][c+2] == col and (c-1 < 0 or grid[r][c-1] != col):
                    bars.append(('h', r, c, col))
                if r + 2 < h and grid[r+1][c] == col and grid[r+2][c] == col and (r-1 < 0 or grid[r-1][c] != col):
                    bars.append(('v', r, c, col))
    def sign(x):
        return (x > 0) - (x < 0)
    for orient, r, c, col in bars:
        if orient == 'h':
            mr, mc = r, c+1
            dr, dc = sign(ar - mr), 0
        else:
            mr, mc = r+1, c
            dr, dc = 0, sign(ac - mc)
        pr, pc = mr + dr, mc + dc
        if orient == 'h':
            for k in (-1, 0, 1):
                cc = pc + k
                if 0 <= pr < h and 0 <= cc < w and grid[pr][cc] != col:
                    res[pr][cc] = 2
        else:
            for k in (-1, 0, 1):
                rr = pr + k
                if 0 <= rr < h and 0 <= pc < w and grid[rr][pc] != col:
                    res[rr][pc] = 2
        r0, c0 = pr, pc
        while (r0, c0) != (ar, ac):
            if grid[r0][c0] != col:
                res[r0][c0] = 2
            r0 += dr
            c0 += dc
    return res