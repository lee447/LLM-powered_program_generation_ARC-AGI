def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs8 = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    # find all 1-components
    seen = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j]==1 and not seen[i][j]:
                stack = [(i,j)]
                seen[i][j] = True
                comp = []
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        rr,cc = r+dr, c+dc
                        if 0<=rr<H and 0<=cc<W and grid[rr][cc]==1 and not seen[rr][cc]:
                            seen[rr][cc] = True
                            stack.append((rr,cc))
                comps.append(comp)
    out = [row[:] for row in grid]
    for comp in comps:
        rs = [r for r,_ in comp]
        cs = [c for _,c in comp]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        box_area = (r1-r0+1)*(c1-c0+1)
        filled = (len(comp)==box_area)
        if filled:
            levels = [(1,2)]
        else:
            levels = [(2,6),(1,8),(0,2)]
        for offset, col in levels:
            rr0, rr1 = r0-offset, r1+offset
            cc0, cc1 = c0-offset, c1+offset
            for c in range(cc0, cc1+1):
                if 0<=rr0<H and 0<=c<W and out[rr0][c]==4: out[rr0][c]=col
                if 0<=rr1<H and 0<=c<W and out[rr1][c]==4: out[rr1][c]=col
            for r in range(rr0, rr1+1):
                if 0<=r<H and 0<=cc0<W and out[r][cc0]==4: out[r][cc0]=col
                if 0<=r<H and 0<=cc1<W and out[r][cc1]==4: out[r][cc1]=col
    return out