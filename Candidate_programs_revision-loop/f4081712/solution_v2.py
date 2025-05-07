def solve(grid):
    R=len(grid); C=len(grid[0])
    from collections import defaultdict
    # find mask color
    mask_color=None
    for color in set(x for row in grid for x in row):
        coords=[(r,c) for r in range(R) for c in range(C) if grid[r][c]==color]
        if len(coords)>1:
            rs=[r for r,c in coords]; cs=[c for r,c in coords]
            r0,r1=min(rs),max(rs); c0,c1=min(cs),max(cs)
            area=(r1-r0+1)*(c1-c0+1)
            if area==len(coords):
                mask_color=color; br0,br1,bc0,bc1=r0,r1,c0,c1
                break
    h=br1-br0+1; w=bc1-bc0+1
    counts=defaultdict(int)
    for r in range(R-h+1):
        for c in range(C-w+1):
            if r<=br1 and r+h-1>=br0 and c<=bc1 and c+w-1>=bc0:
                continue
            good=True
            for i in range(h):
                for j in range(w):
                    if grid[r+i][c+j]==mask_color:
                        good=False; break
                if not good: break
            if not good: continue
            pat=tuple(tuple(grid[r+i][c+j] for j in range(w)) for i in range(h))
            counts[pat]+=1
    best=max(counts, key=counts.get)
    return [list(row) for row in best]