from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5 and not vis[i][j]:
                q = [(i,j)]
                vis[i][j] = True
                comp = [(i,j)]
                while q:
                    x,y = q.pop()
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not vis[nx][ny] and grid[nx][ny] == 5:
                            vis[nx][ny] = True
                            q.append((nx,ny))
                            comp.append((nx,ny))
                comps.append(comp)
    out = [row[:] for row in grid]
    for comp in comps:
        rs = [r for r,c in comp]
        cs = [c for r,c in comp]
        minr, maxr = min(rs), max(rs)
        minc, maxc = min(cs), max(cs)
        height = maxr - minr + 1
        length = height + 1
        for r in range(minr, maxr+1):
            for c in range(minc, maxc+1):
                if out[r][c] == 0:
                    out[r][c] = 2
        r = minr - 1
        left_space = minc
        right_space = w - 1 - maxc
        if left_space < right_space:
            start = 0
        else:
            start = w - length
        if 0 <= r < h:
            for c in range(start, start + length):
                if 0 <= c < w and out[r][c] == 0:
                    out[r][c] = 2
    return out