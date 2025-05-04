def solve(grid):
    H, W = len(grid), len(grid[0])
    greys = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 5]
    (r1, c1), (r2, c2) = greys
    if r1 > r2:
        (r1, c1), (r2, c2) = (r2, c2), (r1, c1)
    reds = {}
    for r, c in greys:
        tmp = []
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            rr, cc = r+dr, c+dc
            if 0 <= rr < H and 0 <= cc < W and grid[rr][cc] == 2:
                tmp.append((rr, cc))
        reds[(r, c)] = tmp
    # vertical bounds
    up_arm = max(rr for rr, _ in reds[(r1, c1)])
    down_arm = min(rr for rr, _ in reds[(r2, c2)])
    # horizontal bounds
    if c1 < c2:
        left_arm = max(cc for _, cc in reds[(r1, c1)])
        right_arm = min(cc for _, cc in reds[(r2, c2)])
    else:
        left_arm = max(cc for _, cc in reds[(r2, c2)])
        right_arm = min(cc for _, cc in reds[(r1, c1)])
    for i in range(up_arm, down_arm+1):
        for j in range(left_arm, right_arm+1):
            if grid[i][j] == 0:
                grid[i][j] = 4
    return grid