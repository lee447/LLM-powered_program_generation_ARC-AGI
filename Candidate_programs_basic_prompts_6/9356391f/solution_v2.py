def solve(grid):
    h=len(grid); w=len(grid[0])
    row0=grid[0]
    run=[]
    run_end=None
    for x in range(w):
        if row0[x]!=0 and run_end is None:
            run.append(row0[x])
        elif run and run_end is None:
            run_end=x-1
    if run_end is None and run:
        run_end=len(run)-1
    b1=None
    for x in range(run_end+1,w):
        if row0[x]!=0:
            b1=(0,x); break
    zeros_count=0
    if b1:
        for x in range(run_end+1,b1[1]):
            if row0[x]==0:
                zeros_count+=1
    b2=None
    for y in range(h):
        for x in range(w):
            if grid[y][x]!=0:
                if y==0 and x<=run_end: continue
                if b1 and y==b1[0] and x==b1[1]: continue
                b2=(y,x)
    ring_colors=[]
    if b1:
        ring_colors.append(grid[b1[0]][b1[1]])
        for _ in range(zeros_count):
            ring_colors.append(0)
    for c in reversed(run):
        ring_colors.append(c)
    radius=len(ring_colors)-1
    cy,cx=b2
    out=[row[:] for row in grid]
    for y in range(h):
        for x in range(w):
            d=max(abs(y-cy),abs(x-cx))
            if d<=radius:
                out[y][x]=ring_colors[radius-d]
    return out