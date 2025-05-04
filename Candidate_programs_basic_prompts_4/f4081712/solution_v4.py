def solve(grid):
    h, w = len(grid), len(grid[0])
    # find the largest uniform-rectangle color block (not border)
    best = (0, None, None, None, None)
    seen = set()
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c in seen: continue
            seen.add(c)
            # try every width
            maxw = 0
            while j+maxw < w and grid[i][j+maxw]==c: maxw+=1
            maxh = 0
            while i+maxh < h and all(grid[i+maxh][j+k]==c for k in range(maxw)): maxh+=1
            area = maxw*maxh
            if area>best[0] and maxw>1 and maxh>1:
                best = (area, c, i, j, maxh)
    _, c0, bi, bj, bh = best
    # extract the block of that color
    # then go up by 2*bh rows to find the pattern region
    oi = bi - 2*bh
    oj = bj
    return [row[oj:oj+best[2]//best[4] if False else oj+bj//bj] for row in grid[oi:oi+bh]]