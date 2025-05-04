import collections
def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    dirs = ((1,0),(-1,0),(0,1),(0,-1))
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==8 and not vis[i][j]:
                stack = [(i,j)]
                vis[i][j] = True
                comp = []
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==8:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                comps.append(comp)
    comp = max(comps, key=len)
    rows = [r for r,c in comp]; cols = [c for r,c in comp]
    minr, maxr = min(rows), max(rows)
    minc, maxc = min(cols), max(cols)
    H, W = maxr-minr+1, maxc-minc+1
    cnt = {}
    best, bestn = None, 0
    for i in range(h-H+1):
        for j in range(w-W+1):
            ok = True
            for ii in range(i, i+H):
                for jj in range(j, j+W):
                    if grid[ii][jj]==8:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            block = tuple(tuple(grid[ii][jj] for jj in range(j, j+W)) for ii in range(i, i+H))
            n = cnt.get(block, 0)+1
            cnt[block] = n
            if n>bestn:
                bestn = n
                best = block
    return [list(r) for r in best]