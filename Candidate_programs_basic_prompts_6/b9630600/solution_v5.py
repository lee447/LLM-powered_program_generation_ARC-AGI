def solve(grid):
    h = len(grid)
    w = len(grid[0])
    visited = [[False]*w for _ in range(h)]
    rects = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==3 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc = r+dr,c+dc
                        if 0<=rr<h and 0<=cc<w and not visited[rr][cc] and grid[rr][cc]==3:
                            visited[rr][cc] = True
                            stack.append((rr,cc))
                rs = [r for r,c in cells]
                cs = [c for r,c in cells]
                r1,r2 = min(rs),max(rs)
                c1,c2 = min(cs),max(cs)
                rects.append((r1,c1,r2,c2))
    bands = {}
    for r1,c1,r2,c2 in rects:
        bands.setdefault(r1,[]).append((r1,c1,r2,c2))
    out = [row[:] for row in grid]
    for band in bands.values():
        band.sort(key=lambda x: x[1])
        n = len(band)
        if n>2:
            r_top = band[0][0]
            r_bot = band[0][2]
            for stripe_row in (r_top+1, r_bot-1):
                for (r1,c1,r2,c2),(r1b,c1b,r2b,c2b) in zip(band,band[1:]):
                    for cc in range(c1+1, c1b):
                        out[stripe_row][cc] = 3
        elif n==2:
            (r1,c1,r2,c2),(r1b,c1b,r2b,c2b) = band
            top = r1+1
            for cc in range(c1+1, c2):
                out[top][cc] = 3
            bot = r2b-1
            for cc in range(c1b+1, c2b):
                out[bot][cc] = 3
        else:
            r1,c1,r2,c2 = band[0]
            stripe = r1+1
            w_int = c2-c1-1
            if w_int%2==1:
                center = c1+1 + w_int//2
                for cc in range(c1+1, c2):
                    if cc!=center:
                        out[stripe][cc] = 3
            else:
                for cc in range(c1+1, c2):
                    out[stripe][cc] = 3
    return out