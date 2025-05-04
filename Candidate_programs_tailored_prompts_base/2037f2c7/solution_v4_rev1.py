from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    # find all "small" 3×3 squares with center==6 and border==4
    centers = []
    for r in range(1, H - 1):
        for c in range(1, W - 1):
            if grid[r][c] == 6:
                ok = True
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == dc == 0: continue
                        if grid[r+dr][c+dc] != 4:
                            ok = False
                if ok:
                    centers.append((r, c))
    if not centers:
        return []
    ys = sorted({r for r, _ in centers})
    xs = sorted({c for _, c in centers})
    m, n = len(ys), len(xs)
    # map each center to pixel coords (i,j)
    pix = [[0]*n for _ in range(m)]
    yi = {y:i for i,y in enumerate(ys)}
    xi = {x:j for j,x in enumerate(xs)}
    for r,c in centers:
        pix[yi[r]][xi[c]] = 1
    # build the border mask of the m×n pixel grid
    mask = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i==0 or i==m-1 or j==0 or j==n-1:
                mask[i][j] = 1
    # find horizontal spacing from input
    if n>1:
        diffs = [xs[i+1]-xs[i] for i in range(n-1)]
        span = diffs[0]
        tile_w = 2
        pad = span//3
    else:
        tile_w = 2
        pad = 2
    Hout = m
    Wout = n*tile_w + (n-1)*pad
    out = [[0]*Wout for _ in range(Hout)]
    for i in range(m):
        for j in range(n):
            if mask[i][j]:
                x0 = j*(tile_w+pad)
                for dx in range(tile_w):
                    out[i][x0+dx] = 8
    return out