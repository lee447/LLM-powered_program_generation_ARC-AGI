def solve(grid):
    h,len_row = len(grid), len(grid[0])
    w = len_row
    res = [row[:] for row in grid]
    shape4 = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==4]
    rmin = min(r for r,c in shape4); rmax = max(r for r,c in shape4)
    cmin = min(c for r,c in shape4); cmax = max(c for r,c in shape4)
    base = [(r-rmin,c-cmin) for r,c in shape4]
    H,W = rmax-rmin+1, cmax-cmin+1
    rots = []
    for rot in range(4):
        s=set()
        for y,x in base:
            if rot==0: y2,x2=y,x
            elif rot==1: y2,x2=x,W-1-y
            elif rot==2: y2,x2=H-1-y,W-1-x
            else: y2,x2=H-1-x,y
            s.add((y2,x2))
        miny = min(y for y,x in s); minx = min(x for y,x in s)
        norm = set((y-miny,x-minx) for y,x in s)
        rots.append(norm)
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c>1 and c!=4 and not visited[i][j]:
                comp = []
                stack = [(i,j)]
                visited[i][j]=True
                while stack:
                    y,x = stack.pop()
                    comp.append((y,x))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx = y+dy,x+dx
                        if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==c:
                            visited[ny][nx]=True
                            stack.append((ny,nx))
                comp_set = set(comp)
                for s in rots:
                    found = False
                    for py,px in comp:
                        for sy,sx in s:
                            dy,dx = py-sy, px-sx
                            trans = set((y+dy,x+dx) for y,x in s)
                            if comp_set.issubset(trans):
                                for y2,x2 in trans-comp_set:
                                    res[y2][x2]=c
                                found = True
                                break
                        if found: break
                    if found: break
    return res