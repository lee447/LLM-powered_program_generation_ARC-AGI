from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    vis = [[False]*W for _ in range(H)]
    comps = []
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    for r in range(H):
        for c in range(W):
            if grid[r][c]==3 and not vis[r][c]:
                stack = [(r,c)]
                vis[r][c] = True
                pts = []
                while stack:
                    x,y = stack.pop()
                    pts.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<H and 0<=ny<W and not vis[nx][ny] and grid[nx][ny]==3:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                minr = min(x for x,y in pts)
                maxr = max(x for x,y in pts)
                minc = min(y for x,y in pts)
                maxc = max(y for x,y in pts)
                comps.append((minr, maxr, minc, maxc))
    comps.sort()
    res = [row[:] for row in grid]
    for i,(minr,maxr,minc,maxc) in enumerate(comps):
        h = maxr-minr+1
        w = maxc-minc+1
        # choose orientation by aspect ratio (rectangles), tie -> horizontal
        if w < h:
            # horizontal
            mag = w+1
            shifts = [(0, mag), (0, -mag)]
        elif w > h:
            # vertical
            mag = h+1
            shifts = [(mag, 0), (-mag, 0)]
        else:
            # square -> horizontal
            mag = w+1
            shifts = [(0, mag), (0, -mag)]
        color = 1 if i%2==0 else 8
        placed = False
        for dr,dc in shifts:
            nr0, nr1 = minr+dr, maxr+dr
            nc0, nc1 = minc+dc, maxc+dc
            if nr0<0 or nr1>=H or nc0<0 or nc1>=W:
                continue
            ok = True
            for rr in range(nr0, nr1+1):
                for cc in range(nc0, nc1+1):
                    if grid[rr][cc] != 0:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            # draw frame
            for rr in range(nr0, nr1+1):
                res[rr][nc0] = color
                res[rr][nc1] = color
            for cc in range(nc0, nc1+1):
                res[nr0][cc] = color
                res[nr1][cc] = color
            placed = True
            break
    return res