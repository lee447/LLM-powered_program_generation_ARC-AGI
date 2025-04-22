def solve(grid):
    rows=len(grid); cols=len(grid[0])
    row_seps=[i for i in range(rows) if all(grid[i][j]==0 for j in range(cols))]
    col_seps=[j for j in range(cols) if all(grid[i][j]==0 for i in range(rows))]
    m=row_seps[1]-row_seps[0]-1
    lps=set()
    for dr,dc in [(0,0),(0,1),(1,0)]:
        lps.add((dr,dc))
        lps.add((dr,m-1-dc))
        lps.add((m-1-dr,dc))
        lps.add((m-1-dr,m-1-dc))
    out=[row[:] for row in grid]
    for bi in range(len(row_seps)-1):
        for bj in range(len(col_seps)-1):
            sr=row_seps[bi]+1; sc=col_seps[bj]+1
            cells=[grid[sr+r][sc+c] for r in range(m) for c in range(m) if grid[sr+r][sc+c]>0]
            cs=list({*cells})
            if len(cs)!=2: continue
            c1,c2=cs
            sample=next((r,c) for r,c in lps if grid[sr+r][sc+c]>0)
            corner_color=grid[sr+sample[0]][sc+sample[1]]
            fill_color=(c1 if corner_color==c2 else c2) if corner_color in (c1,c2) else None
            if fill_color is None: fill_color=c2
            if (bi+bj)%2==0:
                corner_color,fill_color=fill_color,corner_color
            for r in range(m):
                for c in range(m):
                    if (r,c) in lps:
                        out[sr+r][sc+c]=corner_color
                    else:
                        out[sr+r][sc+c]=fill_color
    return out