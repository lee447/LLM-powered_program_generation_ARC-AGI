from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            c = grid[i][j]
            if c and not seen[i][j]:
                q = [(i,j)]
                seen[i][j] = True
                pts = []
                for x,y in q:
                    pts.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not seen[nx][ny] and grid[nx][ny]==c:
                            seen[nx][ny]=True
                            q.append((nx,ny))
                rs = [x for x,y in pts]; cs = [y for x,y in pts]
                r0,r1 = min(rs), max(rs)
                c0,c1 = min(cs), max(cs)
                h,w = r1-r0+1, c1-c0+1
                area = h*w
                if area==len(pts) and area>1:
                    comps.append((c,r0,r1,c0,c1))
    counts = {}
    for c,r0,r1,c0,c1 in comps:
        key = (c, r1-r0+1, c1-c0+1)
        counts[key] = counts.get(key,0)+1
    out = [[0]*W for _ in range(H)]
    for c,r0,r1,c0,c1 in comps:
        key = (c, r1-r0+1, c1-c0+1)
        if counts.get(key,0)>=2:
            for x in range(r0,r1+1):
                for y in range(c0,c1+1):
                    out[x][y] = c
    return out