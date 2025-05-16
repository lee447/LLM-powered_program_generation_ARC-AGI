def solve(grid):
    h=len(grid)
    w=len(grid[0])
    border=grid[0][0]
    brs=[r for r in range(h) if all(grid[r][c]==border for c in range(w))]
    bcs=[c for c in range(w) if all(grid[r][c]==border for r in range(h))]
    bh=brs[1]-brs[0]-1
    bw=bcs[1]-bcs[0]-1
    rows=len(brs)-1
    cols=len(bcs)-1
    def get_pattern(i,j):
        return tuple(tuple(grid[r][c] for c in range(bcs[j]+1,bcs[j+1])) for r in range(brs[i]+1,brs[i+1]))
    base=[get_pattern(0,j) for j in range(cols)]
    changed=[None]*cols
    for j in range(cols):
        for i in range(1,rows):
            p=get_pattern(i,j)
            if p!=base[j]:
                changed[j]=p
                break
    out=[row[:] for row in grid]
    for j in range(cols):
        if changed[j] is not None:
            for i in range(rows):
                for di,r in enumerate(range(brs[i]+1,brs[i+1])):
                    for dj,c in enumerate(range(bcs[j]+1,bcs[j+1])):
                        out[r][c]=changed[j][di][dj]
    return out