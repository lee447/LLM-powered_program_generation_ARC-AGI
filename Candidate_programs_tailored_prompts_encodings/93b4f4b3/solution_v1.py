def solve(grid):
    h = len(grid)
    w = len(grid[0])
    C = 6
    bg = grid[0][0]
    stripes = [r for r in range(h) if all(grid[r][c] == bg for c in range(C))]
    out = [[0]*C for _ in range(h)]
    for r in range(h):
        for c in range(C):
            out[r][c] = grid[r][c]
    for i in range(len(stripes)-1):
        top = stripes[i]+1
        bot = stripes[i+1]
        band = list(range(top, bot))
        cells = [(r,c,grid[r][c]) for r in band for c in range(C, w) if grid[r][c]!=bg and grid[r][c]!=0]
        if not cells: continue
        col_vals = {v for _,_,v in cells}
        color = col_vals.pop() if len(col_vals)==1 else None
        row_widths = []
        for r in band:
            cnt = len([1 for rr,cc,v in cells if rr==r])
            row_widths.append(cnt)
        maxw = max(row_widths)
        for idx,r in enumerate(band):
            wi = row_widths[idx]
            if wi==0: continue
            off = (C - wi)//2
            for cc in range(off, off+wi):
                out[r][cc] = color
    return out