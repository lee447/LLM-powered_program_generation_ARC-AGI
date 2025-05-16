from collections import Counter
def solve(grid):
    h,w=len(grid),len(grid[0])
    bg=grid[0][0]
    out=[row[:] for row in grid]
    threshold=h//3
    row_groups={}
    for r in range(h):
        cs=[c for c in range(w) if grid[r][c]!=bg]
        if cs:
            row_groups[r]=sorted(cs)
    cs_counts=Counter(tuple(cs) for cs in row_groups.values())
    for v in set(grid[r][c] for r in range(h) for c in range(w) if grid[r][c]!=bg):
        for r0,cs in row_groups.items():
            if r0<threshold or r0==h-1:continue
            if any(grid[r0][c]==v for c in cs)==False:continue
            runs=[]
            cur=[cs[0]]
            for c in cs[1:]:
                if c==cur[-1]+1:
                    cur.append(c)
                else:
                    runs.append(cur)
                    cur=[c]
            runs.append(cur)
            if cs_counts[tuple(cs)]>1 and all(len(run)==1 for run in runs):
                continue
            n=len(cs)
            if n==2:continue
            r1=r0-threshold
            hl=1 if v==9 else 9
            if any(len(run)>=2 for run in runs):
                if len(runs)>1:
                    starts=[run[0] for run in runs]
                    spacing=starts[1]-starts[0]
                    for i in range(len(starts)):
                        c1=i*spacing
                        if 0<=c1<w:
                            out[r1][c1]=hl
                continue
            if n==1:
                new_cs=[cs[0]]
            elif n==3:
                if v==9:
                    new_cs=[cs[1]]
                else:
                    new_cs=[cs[-1] if r1%2==0 else cs[0]]
            elif n%2==0:
                m=n//2
                new_cs=cs[:m] if r1%2==1 else cs[m:]
            else:
                new_cs=[cs[n//2]]
            for c1 in new_cs:
                if 0<=c1<w:
                    out[r1][c1]=hl
    return out