from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bar_r = bar_c = 0
    L = 0
    for r in range(h):
        c = 0
        while c < w:
            if grid[r][c] == 8:
                start = c
                while c < w and grid[r][c] == 8:
                    c += 1
                length = c - start
                if length >= 3 and length > L:
                    L, bar_r, bar_c = length, r, start
            else:
                c += 1
    center_r, center_c = bar_r, bar_c + L // 2
    dirs = {
        'left': (0, -1),
        'right': (0, 1),
        'up': (-1, 0),
        'down': (1, 0)
    }
    free = {}
    for name, (dr, dc) in dirs.items():
        if name == 'left':
            rr, cc = bar_r, bar_c - 1
        elif name == 'right':
            rr, cc = bar_r, bar_c + L
        elif name == 'up':
            rr, cc = bar_r - 1, center_c
        else:
            rr, cc = bar_r + 1, center_c
        cnt = 0
        while 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 0:
            cnt += 1
            rr += dr
            cc += dc
        free[name] = cnt
    m = max(free.values())
    direction = next((n for n in free if free[n] == m and m > 0), 'down')
    dr, dc = dirs[direction]
    if direction == 'left':
        rr, cc = bar_r, bar_c - 1
    elif direction == 'right':
        rr, cc = bar_r, bar_c + L
    elif direction == 'up':
        rr, cc = bar_r - 1, center_c
    else:
        rr, cc = bar_r + 1, center_c
    while 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 0:
        rr += dr
        cc += dc
    nr = min(max(rr, 0), h - 1)
    nc = min(max(cc, 0), w - 1)
    dcr = nr - center_r
    dcc = nc - center_c
    new_r = bar_r + dcr
    new_c0 = bar_c + dcc
    for j in range(L):
        nrj = new_r
        ncj = new_c0 + j
        if 0 <= nrj < h and 0 <= ncj < w and grid[nrj][ncj] == 0:
            grid[nrj][ncj] = 8
    return grid