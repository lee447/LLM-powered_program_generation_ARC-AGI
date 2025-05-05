def solve(grid):
    H, W = len(grid), len(grid[0])
    bar_rows = [r for r in range(H) if sum(1 for j in range(W) if grid[r][j] != 0) >= 3]
    pivots = sorted(j for j in range(W) if all(grid[r][j] == 0 for r in bar_rows) and any(grid[r][j] != 0 for r in range(H) if r not in bar_rows))
    a1, a2 = pivots
    leftColor = {}
    rightColor = {}
    for r in bar_rows:
        for j in range(a1):
            if grid[r][j] != 0:
                leftColor[r] = grid[r][j]
                break
        for j in range(W - 1, a2, -1):
            if grid[r][j] != 0:
                rightColor[r] = grid[r][j]
                break
    nonb = set(range(H)) - set(bar_rows)
    bl = [r for r in nonb if grid[r][a1] != 0]
    br = [r for r in nonb if grid[r][a2] != 0]
    bottomLeft = max(bl) if bl else None
    bottomRight = max(br) if br else None
    out = [[0]*W for _ in range(H)]
    for r in bar_rows:
        if r in leftColor:
            js = [j for j in range(a2) if grid[r][j] == leftColor[r]]
            mn, mx = min(js), max(js)
            for j in range(mn, mx+1):
                out[r][j] = leftColor[r]
        if r in rightColor:
            js = [j for j in range(a1+1, W) if grid[r][j] == rightColor[r]]
            mn, mx = min(js), max(js)
            for j in range(mn, mx+1):
                out[r][j] = rightColor[r]
    barsL = sorted(leftColor)
    chainL = barsL + ([bottomLeft] if bottomLeft is not None else [])
    chainL = sorted(chainL)
    prev = -1
    for r in chainL:
        c = leftColor[r] if r in leftColor else grid[r][a1]
        for i in range(prev+1, r+1):
            out[i][a1] = c
        prev = r
    barsR = sorted(rightColor)
    chainR = barsR + ([bottomRight] if bottomRight is not None else [])
    chainR = sorted(chainR)
    prev = -1
    for r in chainR:
        c = rightColor[r] if r in rightColor else grid[r][a2]
        for i in range(prev+1, r+1):
            out[i][a2] = c
        prev = r
    return out