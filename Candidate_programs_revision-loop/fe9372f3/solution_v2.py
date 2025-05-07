def solve(grid):
    h, w = len(grid), len(grid[0])
    cr = cc = None
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 2 and 0 < r < h-1 and 0 < c < w-1:
                if grid[r-1][c] == 2 and grid[r+1][c] == 2 and grid[r][c-1] == 2 and grid[r][c+1] == 2:
                    cr, cc = r, c
                    break
        if cr is not None:
            break
    arm = 0
    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
        cnt = 0
        while True:
            nr = cr + dr*(cnt+1)
            nc = cc + dc*(cnt+1)
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 2:
                cnt += 1
            else:
                break
        arm = max(arm, cnt)
    out = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            dv = abs(i-cr)
            dh = abs(j-cc)
            if grid[i][j] == 2:
                out[i][j] = 2
            elif dv <= arm and dh <= arm:
                out[i][j] = 1
            elif dv == dh or dv == 0 or dh == 0:
                k = dv if dv > dh else dh
                if dv == dh:
                    out[i][j] = 1
                else:
                    if k >= 2 and k % 3 == 1:
                        out[i][j] = 4
                    else:
                        out[i][j] = 8
            else:
                out[i][j] = 0
    return out