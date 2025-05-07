def solve(grid):
    h=len(grid);w=len(grid[0])
    blocks=[]
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2:
                blocks.append((r,c))
    cols={}
    for r,c in blocks:
        cols.setdefault(c,[]).append((r,c))
    sorted_cols=sorted(cols.keys(),reverse=True)
    rec_cols={c for i,c in enumerate(sorted_cols) if i%2==0}
    out=[row[:] for row in grid]
    for c in rec_cols:
        for r,_ in cols[c]:
            out[r][c]=8;out[r][c+1]=8;out[r+1][c]=8;out[r+1][c+1]=8
    return out