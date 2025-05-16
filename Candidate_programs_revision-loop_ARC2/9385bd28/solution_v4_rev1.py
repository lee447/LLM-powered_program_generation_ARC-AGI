from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    def find_comps(color):
        seen = [[False]*w for _ in range(h)]
        comps = []
        for i in range(h):
            for j in range(w):
                if not seen[i][j] and grid[i][j] == color:
                    q = deque([(i,j)])
                    seen[i][j] = True
                    comp = [(i,j)]
                    while q:
                        x,y = q.popleft()
                        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            nx,ny = x+dx, y+dy
                            if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==color:
                                seen[nx][ny]=True
                                q.append((nx,ny))
                                comp.append((nx,ny))
                    comps.append(comp)
        return comps

    def is_L(comp):
        if len(comp)!=3:
            return False
        s = set(comp)
        deg = [sum(((x+dx,y+dy) in s) for dx,dy in ((1,0),(-1,0),(0,1),(0,-1))) for x,y in comp]
        return sorted(deg)==[1,1,2]

    def vertical_endpoint(comp):
        s = set(comp)
        for x,y in comp:
            cnt = sum(((x+dx,y+dy) in s) for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)))
            if cnt==2:
                for dx,dy in ((1,0),(-1,0)):
                    nx,ny = x+dx,y+dy
                    if (nx,ny) in s:
                        return (nx,ny)
        return None

    candidates = []
    for color in set(v for row in grid for v in row if v!=0):
        pcs = [c for c in find_comps(color) if is_L(c)]
        if len(pcs)==2:
            eps = [vertical_endpoint(c) for c in pcs]
            if None not in eps:
                (r1,c1),(r2,c2) = eps
                area = (abs(r2-r1)+1)*(abs(c2-c1)+1)
                candidates.append((area,color,(r1,c1),(r2,c2)))
    if not candidates:
        return grid
    _,col,rp1,rp2 = max(candidates,key=lambda x:x[0])
    r1,c1 = rp1; r2,c2 = rp2
    rmin,rmax = min(r1,r2), max(r1,r2)
    cmin,cmax = min(c1,c2), max(c1,c2)
    bc = max(v for row in grid for v in row)
    out = [row[:] for row in grid]
    for i in range(rmin,rmax+1):
        for j in range(cmin,cmax+1):
            if i in (rmin,rmax) or j in (cmin,cmax):
                if out[i][j]!=col:
                    out[i][j]=bc
    return out