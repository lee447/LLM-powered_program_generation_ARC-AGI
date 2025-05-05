def solve(grid):
    H, W = len(grid), len(grid[0])
    rows = []
    inside = False
    for i in range(H):
        if any(grid[i][j] != 0 for j in range(W)):
            if not inside:
                inside = True
                r0 = i
        else:
            if inside:
                rows.append((r0, i - 1))
                inside = False
    if inside:
        rows.append((r0, H - 1))
    cols = []
    inside = False
    for j in range(W):
        if any(grid[i][j] != 0 for i in range(H)):
            if not inside:
                inside = True
                c0 = j
        else:
            if inside:
                cols.append((c0, j - 1))
                inside = False
    if inside:
        cols.append((c0, W - 1))
    res = [row[:] for row in grid]
    for c0, c1 in cols:
        top0, top1 = rows[0]
        bot0, bot1 = rows[-1]
        pts = []
        for di in range(1, top1 - top0):
            for dj in range(1, c1 - c0):
                if grid[top0 + di][c0 + dj] != 0:
                    pts.append((di - 1, dj - 1))
        if not pts:
            pts = [(1,1)]
        color = grid[bot0][c0]
        for di, dj in pts:
            for ddi, ddj in [(0,0),(1,0),(-1,0),(0,1),(0,-1)]:
                ni, nj = di + ddi, dj + ddj
                if 0 <= ni < (bot1 - bot0 - 1) and 0 <= nj < (c1 - c0 - 1):
                    res[bot0 + 1 + ni][c0 + 1 + nj] = color
    return res