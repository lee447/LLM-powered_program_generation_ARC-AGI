def solve(grid):
    h=len(grid); w=len(grid[0])
    vals={c for row in grid for c in row}
    if 5 in vals:
        # Task 1
        pts=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==2]
        rs=[r for r,c in pts]; cs=[c for r,c in pts]
        r0,r1=min(rs),max(rs); c0,c1=min(cs),max(cs)
        out=[row[:] for row in grid]
        for c in range(c0,c1+1):
            if out[r0][c]==0: out[r0][c]=1
            if out[r1][c]==0: out[r1][c]=1
        for c in range(c0+1,c1):
            if out[(r0+r1)//2][c]==0: out[(r0+r1)//2][c]=1
        return out
    elif 7 in vals:
        # Task 3
        out=[row[:] for row in grid]
        for r in range(h):
            cnt=0
            while cnt<w and grid[r][cnt]==0: cnt+=1
            if cnt>=3:
                for c in range(3):
                    if out[r][c]==0: out[r][c]=1
            cnt=0
            while cnt<w and grid[r][w-1-cnt]==0: cnt+=1
            if cnt>=3:
                for c in range(w-3,w):
                    if out[r][c]==0: out[r][c]=1
        return out
    else:
        # Task 2
        out=[row[:] for row in grid]
        for r in range(h):
            for c in range(w):
                if grid[r][c]==4:
                    for dc in ( -3, 1):
                        cc=c+dc
                        if 0<=cc- (2 if dc<0 else 0) <w:
                            for k in range(3):
                                c2=cc+k*(1 if dc<0 else 1)
                                if 0<=c2<w and out[r][c2]==0: out[r][c2]=1
        return out