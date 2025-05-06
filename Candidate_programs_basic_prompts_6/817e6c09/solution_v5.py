def solve(grid):
    h=len(grid); w=len(grid[0])
    blocks=[]
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2:
                blocks.append((r,c))
    blocks.sort(key=lambda x:(x[1],x[0]))
    n=len(blocks)
    out=[row[:] for row in grid]
    for i,(r,c) in enumerate(blocks):
        if (n%2==1 and i%2==0) or (n%2==0 and i%2==1):
            out[r][c]=8; out[r][c+1]=8; out[r+1][c]=8; out[r+1][c+1]=8
    return out