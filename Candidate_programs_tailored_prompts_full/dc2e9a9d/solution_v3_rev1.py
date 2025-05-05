from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    def find_hollow(c: int) -> List[Tuple[int,int,int]]:
        seen = [[False]*w for _ in range(h)]
        out = []
        for r in range(h):
            for cc in range(w):
                if not seen[r][cc] and grid[r][cc]==c:
                    stack = [(r,cc)]
                    pts = []
                    seen[r][cc]=True
                    while stack:
                        x,y = stack.pop()
                        pts.append((x,y))
                        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            nx,ny = x+dx, y+dy
                            if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==c:
                                seen[nx][ny]=True
                                stack.append((nx,ny))
                    rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
                    r0,r1 = min(rs), max(rs); c0,c1 = min(cs), max(cs)
                    szr = r1-r0+1; szc = c1-c0+1
                    if szr==szc and szr>=3:
                        good = True
                        for i in range(szr):
                            for j in range(szc):
                                v = grid[r0+i][c0+j]
                                if i in (0,szr-1) or j in (0,szc-1):
                                    if v!=c: good=False; break
                                else:
                                    if v==c: good=False; break
                            if not good: break
                        if good:
                            out.append((r0,c0,szr))
        return out
    greens = find_hollow(3)
    greens.sort(key=lambda x: x[0])
    if not greens:
        return grid
    if len(greens)>=3:
        top, mid = greens[0], greens[1]
        r0,c0,s0 = top
        cb = c0+s0+1
        for i in range(s0):
            for j in range(s0):
                grid[r0+i][cb+j] = 1
        r1,c1,s1 = mid
        rb = r1 + s1
        for i in range(s1):
            for j in range(s1):
                if i in (0,s1-1) or j in (0,s1-1):
                    grid[rb+i][c1+j] = 8
    else:
        a0,a1 = greens[0], greens[1]
        r0,c0,s0 = a0; r1,c1,s1 = a1
        rb = r0 + s0 + 1
        for i in range(s1):
            for j in range(s1):
                if i in (0,s1-1) or j in (0,s1-1):
                    grid[rb+i][c1+j] = 8
    return grid