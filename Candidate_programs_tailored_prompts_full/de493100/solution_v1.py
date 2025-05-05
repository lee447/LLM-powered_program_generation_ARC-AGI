def solve(grid):
    H, W = len(grid), len(grid[0])
    # find connected components
    seen = [[False]*W for _ in range(H)]
    comps = []
    for r in range(H):
        for c in range(W):
            if not seen[r][c]:
                col = grid[r][c]
                stack = [(r,c)]
                seen[r][c] = True
                cells = []
                while stack:
                    i,j = stack.pop()
                    cells.append((i,j))
                    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                        ni,nj = i+di,j+dj
                        if 0<=ni<H and 0<=nj<W and not seen[ni][nj] and grid[ni][nj]==col:
                            seen[ni][nj] = True
                            stack.append((ni,nj))
                rs = [p[0] for p in cells]; cs = [p[1] for p in cells]
                comps.append((col, len(cells), min(rs), max(rs), min(cs), max(cs)))
    # pick comp2 = largest area among color 6 or 7
    cand2 = [c for c in comps if c[0] in (6,7)]
    comp2 = max(cand2, key=lambda x: x[1])
    _,_, r2min,r2max,c2min,c2max = comp2
    # if horizontal band
    if (r2max-r2min) < (c2max-c2min):
        # pick comp1 = left grey cluster if exists else entire top rows
        left5 = [c for c in comps if c[0]==5]
        if left5:
            comp1 = min(left5, key=lambda x: x[4])
            _,_,r1min,r1max,c1min,c1max = comp1
            top = r1min; bot = r2min
        else:
            top = 0; bot = r2min
        out = [row[c2min:c2max+1] for row in grid[top:bot]]
    else:
        # vertical stripe
        # header rows = r2min if mixed else 0
        header = r2min
        out = [row[0:c2min] for row in grid[r2min:r2max+1] if c2min>0]
        if not out:
            out = [row[0:c2min] for row in grid[0:header]]
    return out