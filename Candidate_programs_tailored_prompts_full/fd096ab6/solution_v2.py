def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    seen = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c not in (0,1,4) and not seen[i][j]:
                pts = [(i,j)]
                seen[i][j] = True
                for di in range(h):
                    for dj in range(w):
                        if not seen[di][dj] and grid[di][dj]==c and abs(di-i)+abs(dj-j)<=2:
                            pts.append((di,dj))
                            seen[di][dj]=True
                ci = sum(x for x,y in pts)//len(pts)
                cj = sum(y for x,y in pts)//len(pts)
                for di,dj in dirs+[(0,0)]:
                    ni, nj = ci+di, cj+dj
                    if 0<=ni<h and 0<=nj<w:
                        res[ni][nj] = c
    return res