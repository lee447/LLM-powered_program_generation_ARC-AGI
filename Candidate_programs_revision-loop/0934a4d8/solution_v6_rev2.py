from collections import Counter
def solve(grid):
    R=len(grid);C=len(grid[0])
    pts=[(r,c) for r in range(R) for c in range(C) if grid[r][c]==8]
    if not pts: return grid
    rs=[r for r,c in pts]; cs=[c for r,c in pts]
    r0,r1=min(rs),max(rs); c0,c1=min(cs),max(cs)
    h=r1-r0+1; w=c1-c0+1
    cnt=Counter()
    for r in range(R-h+1):
        for c in range(C-w+1):
            block=[]
            ok=True
            for i in range(h):
                row=grid[r+i][c:c+w]
                if 8 in row:
                    ok=False; break
                block.append(tuple(row))
            if ok:
                cnt[tuple(block)]+=1
    if not cnt: return []
    best=cnt.most_common(1)[0][0]
    return [list(row) for row in best]