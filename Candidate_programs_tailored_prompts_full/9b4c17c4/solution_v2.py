def solve(grid):
    h, w = len(grid), len(grid[0])
    rows_mix = [ (1 in row and 8 in row) for row in grid ]
    vertical = any(rows_mix)
    if vertical:
        best_c, best_cnt = 0, -1
        for c in range(w-1):
            cnt = 0
            for r in range(h):
                a, b = grid[r][c], grid[r][c+1]
                if a in (1,8) and b in (1,8) and a != b:
                    cnt += 1
            if cnt > best_cnt:
                best_cnt, best_c = cnt, c
        seam = best_c
        left_color, right_color = grid[0][0], grid[0][w-1]
    else:
        best_r, best_cnt = 0, -1
        for r in range(h-1):
            cnt = 0
            for c in range(w):
                a, b = grid[r][c], grid[r+1][c]
                if a in (1,8) and b in (1,8) and a != b:
                    cnt += 1
            if cnt > best_cnt:
                best_cnt, best_r = cnt, r
        seam = best_r
        top_color, bot_color = grid[0][0], grid[h-1][0]
    new = [row[:] for row in grid]
    blocks = []
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2:
                blocks.append((r,c))
    for r,c in blocks:
        if vertical:
            zone = left_color if c <= seam else right_color
        else:
            zone = top_color if r <= seam else bot_color
        for dr in (0,1):
            for dc in (0,1):
                new[r+dr][c+dc] = zone
    for r,c in blocks:
        if vertical:
            nc = 2*seam - c
            nr = r
        else:
            nr = 2*seam - r
            nc = c
        for dr in (0,1):
            for dc in (0,1):
                new[nr+dr][nc+dc] = 2
    return new