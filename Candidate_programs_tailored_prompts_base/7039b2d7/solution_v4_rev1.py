from collections import Counter
def solve(grid):
    h,w=len(grid),len(grid[0])
    cnt=Counter(c for row in grid for c in row)
    bg=cnt.most_common(1)[0][0]
    rows=[i for i in range(h) if len({grid[i][j] for j in range(w)})==1 and grid[i][0]!=bg]
    cols=[j for j in range(w) if len({grid[i][j] for i in range(h)})==1 and grid[0][j]!=bg]
    rows.sort(); cols.sort()
    if len(rows)>=2 and len(cols)>=2:
        r0,r1=rows[0],rows[1]
        c0,c1=cols[0],cols[1]
        stripe=grid[r0][0]
        if stripe==bg:
            fill=Counter(grid[i][j] for i in range(r0+1,r1) for j in range(c0+1,c1)).most_common(1)[0][0]
            return [[fill]*(c1-c0-1) for _ in range(r1-r0)]
        return [row[c0+1:c1] for row in grid[r0+1:r1]]
    s0=rows[0] if rows else 0
    height=min(s0,h-s0)//2
    c1,c2=cols[1],cols[2]
    diff=c2-c1
    width=diff//2
    start_row=(s0-height)//2
    start_col=c1+(diff-width)//2
    return [grid[i][start_col:start_col+width] for i in range(start_row,start_row+height)]