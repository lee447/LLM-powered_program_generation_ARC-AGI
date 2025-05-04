def solve(grid):
    h=len(grid);w=len(grid[0])
    out=[row[:] for row in grid]
    active=[any(grid[r][c]!=0 for r in range(h)) for c in range(w)]
    c=0
    while c<w:
        if not active[c]:
            c+=1
            continue
        start=c
        while c<w and active[c]:
            c+=1
        end=c-1
        rows=[r for r in range(h) if any(grid[r][cc]!=0 for cc in range(start,end+1))]
        if not rows:
            continue
        r0,r1=min(rows),max(rows)
        width=end-start+1
        seed=[grid[r][start] for r in range(r0,r1+1)]
        full=[sum(1 for c2 in range(start,end+1) if grid[r][c2]!=0)==width for r in range(r0,r1+1)]
        if all(s==seed[0] and s!=0 for s in seed):
            patterns=[r0+i for i,f in enumerate(full) if f]
            m=len(patterns)
            for i in range(r1-r0+1):
                src=patterns[i%m]
                for cc in range(start,end+1):
                    out[r0+i][cc]=grid[src][cc]
        else:
            for i in range(r1-r0+1):
                r=r0+i
                if full[i]:
                    for cc in range(start,end+1):
                        out[r][cc]=grid[r][cc]
                else:
                    cval=grid[r][start]
                    for cc in range(start,end+1):
                        out[r][cc]=cval
    return out