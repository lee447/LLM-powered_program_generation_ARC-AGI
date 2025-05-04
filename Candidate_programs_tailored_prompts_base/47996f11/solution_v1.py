def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    # find central vertical stripes of 6
    visited = [[False]*w for _ in range(h)]
    stripes = []
    for r in range(h):
        for c in range(w):
            if grid[r][c]==6 and not visited[r][c]:
                # flood-fill component
                stack=[(r,c)]
                comp=[]
                while stack:
                    x,y=stack.pop()
                    if 0<=x<h and 0<=y<w and grid[x][y]==6 and not visited[x][y]:
                        visited[x][y]=True
                        comp.append((x,y))
                        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                            stack.append((x+dx,y+dy))
                if comp:
                    rs=[x for x,y in comp]
                    cs=[y for x,y in comp]
                    r0,r1=min(rs),max(rs)
                    c0,c1=min(cs),max(cs)
                    if (r1-r0+1) > (c1-c0+1):
                        stripes.append((r0,r1,c0,c1))
                    else:
                        # small clusters -> brown
                        for x,y in comp:
                            out[x][y]=9
    # recolor big stripes to 7 and adjust neighbors
    for r0,r1,c0,c1 in stripes:
        for x in range(r0,r1+1):
            for y in range(c0,c1+1):
                out[x][y]=7
        for side in [(-1,0),(1,0)]:
            dc = side[0]
            cc0 = c0+dc
            cc1 = c1+dc
            for cc in [cc0,cc1]:
                run=[]
                for x in range(h):
                    if grid[x][cc]==8:
                        run.append(x)
                        # turn inner edge
                        if x==r0 or x==r1:
                            out[x][cc]=9
                    else:
                        run=[]
    # find 2x2 grey anchors and swap nearby 1/3 clusters
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==5 and grid[r][c+1]==5 and grid[r+1][c]==5 and grid[r+1][c+1]==5:
                for dr in (-2,2):
                    for dc in (-2,2):
                        r0,c0 = r+dr, c+dc
                        if 0<=r0<h-1 and 0<=c0<w-1:
                            block=[grid[r0][c0],grid[r0][c0+1],grid[r0+1][c0],grid[r0+1][c0+1]]
                            if set(block)=={1,3}:
                                for dx in (0,1):
                                    for dy in (0,1):
                                        out[r0+dx][c0+dy] = 1 if grid[r0+dx][c0+dy]==3 else 3
    # trim horizontal bands of 2/8 near each big stripe
    for r in range(h):
        runs=[]
        cur_val=None
        start=0
        for c in range(w+1):
            v = grid[r][c] if c<w else None
            if v==cur_val and (v==2 or v==8):
                continue
            else:
                if cur_val in (2,8):
                    runs.append((start,c-1,cur_val))
                cur_val=v
                start=c
        for c0,c1,val in runs:
            for (r0,r1,c0s,c1s) in stripes:
                if c1+1==c0s:
                    out[r][c1]=None
                if c0-1==c1s:
                    out[r][c0]=None
    # rebuild trimmed None's by shifting
    for r in range(h):
        row = [x for x in out[r] if x is not None]
        while len(row)<w:
            row.insert(0,0)
        out[r]=row
    return out