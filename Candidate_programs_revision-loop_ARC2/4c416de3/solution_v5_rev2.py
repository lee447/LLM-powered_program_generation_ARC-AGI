from typing import List
import collections

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    bg = collections.Counter(c for row in grid for c in row).most_common(1)[0][0]

    def find_rings():
        vis = [[False]*W for _ in range(H)]
        rings = []
        for r in range(H):
            for c in range(W):
                if grid[r][c] != bg and not vis[r][c]:
                    B = grid[r][c]
                    q = [(r,c)]
                    vis[r][c] = True
                    comp = []
                    for x,y in q:
                        comp.append((x,y))
                        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            nx,ny = x+dx,y+dy
                            if 0<=nx<H and 0<=ny<W and not vis[nx][ny] and grid[nx][ny]==B:
                                vis[nx][ny]=True
                                q.append((nx,ny))
                    rs = [x for x,_ in comp]; cs = [y for _,y in comp]
                    r0,r1,minr,maxr = min(rs),max(rs),min(rs),max(rs)
                    c0,c1,minc,maxc = min(cs),max(cs),min(cs),max(cs)
                    h,w = r1-r0+1, c1-c0+1
                    if h>2 and w>2 and len(comp)==2*(h+w-2):
                        # identify interior fill color
                        freq = collections.Counter(grid[i][j] for i in range(r0+1,r1) for j in range(c0+1,c1))
                        F,_ = freq.most_common(1)[0]
                        rings.append((r0,c0,r1,c1,B,F))
        return rings

    rings = find_rings()
    out = [row[:] for row in grid]

    for r0,c0,r1,c1,B,F in rings:
        best = None
        for i in range(r0+1,r1):
            for j in range(c0+1,c1):
                v = grid[i][j]
                if v!=F and v!=B:
                    if best is None or (i,j)<best[0]:
                        best = ((i,j),v)
        if best:
            (ri,ci),v = best
            br = [(r0-1,c0-1),(r0-1,c0),(r0,c0-1),(r0,c0)]
            for x,y in br:
                if 0<=x<H and 0<=y<W and out[x][y]==bg:
                    out[x][y] = v
    return out