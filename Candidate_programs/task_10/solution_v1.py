def solve(grid):
    h, w = len(grid), len(grid[0])
    # find the horizontal bar of three 8s
    for r in range(h):
        for c in range(w-2):
            if grid[r][c] == grid[r][c+1] == grid[r][c+2] == 8:
                bar_r, bar_c = r, c
                break
        else:
            continue
        break
    # compute free space in each direction
    dirs = [('left', (0, -1)), ('up', (-1, 0)), ('down', (1, 0)), ('right', (0, 1))]
    free = {}
    center_r, center_c = bar_r, bar_c+1
    for name, (dr, dc) in dirs:
        # start scanning from just beyond the bar
        if name == 'left':
            rr, cc = bar_r, bar_c-1
        elif name == 'right':
            rr, cc = bar_r, bar_c+3
        else:
            rr, cc = bar_r+dr, center_c
        cnt = 0
        while 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 0:
            cnt += 1
            rr += dr
            cc += dc
        free[name] = cnt
    # choose direction
    m = max(free.values())
    if m > 0:
        for name, _ in dirs:
            if free[name] == m:
                direction = name
                break
    else:
        direction = 'down'
    dr, dc = dict(dirs)[direction]
    # find barrier position: step from just beyond bar until non-zero or outside
    if direction == 'left':
        rr, cc = bar_r, bar_c-1
    elif direction == 'right':
        rr, cc = bar_r, bar_c+3
    else:
        rr, cc = bar_r+dr, center_c
    while 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 0:
        rr += dr
        cc += dc
    # rr,cc is barrier (possibly out of grid)
    br = rr
    bc = cc
    # new center = barrier position clamped
    nr = min(max(br, 0), h-1)
    nc = min(max(bc, 0), w-1)
    # delta from original center
    dcr = nr - center_r
    dcc = nc - center_c
    # place the duplicated bar
    for j in range(3):
        rr = bar_r + dcr
        cc = bar_c + j + dcc
        if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 0:
            grid[rr][cc] = 8
    return grid