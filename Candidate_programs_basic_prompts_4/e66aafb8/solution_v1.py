def solve(grid):
    rows=len(grid)
    cols=len(grid[0])
    r0, r1, c0, c1 = rows, -1, cols, -1
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==0:
                if i<r0: r0=i
                if i>r1: r1=i
                if j<c0: c0=j
                if j>c1: c1=j
    h=r1-r0+1
    w=c1-c0+1
    counts={}
    for i in range(rows-h+1):
        for j in range(cols-w+1):
            block=[]
            ok=True
            for ii in range(i,i+h):
                row=grid[ii][j:j+w]
                if 0 in row:
                    ok=False
                    break
                block.append(tuple(row))
            if ok:
                key=tuple(block)
                counts[key]=counts.get(key,0)+1
    best=max(counts.items(), key=lambda x:(x[1], sum(sum(r) for r in x[0])))[0]
    return [list(r) for r in best]