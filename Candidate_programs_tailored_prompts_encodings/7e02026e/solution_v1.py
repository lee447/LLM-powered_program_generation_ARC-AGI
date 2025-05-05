def solve(grid):
    h=len(grid);w=len(grid[0])
    candidates=[]
    for r in range(1,h-1):
        for c in range(1,w-1):
            if grid[r][c]==0 and grid[r-1][c]==0 and grid[r+1][c]==0 and grid[r][c-1]==0 and grid[r][c+1]==0:
                candidates.append((r,c))
    diag_map={}
    for r,c in candidates:
        diag_map.setdefault(r-c,[]).append((r,c))
    centers=[]
    for d,pts in diag_map.items():
        if len(pts)==2:
            centers=pts
            break
    out=[row[:] for row in grid]
    for r,c in centers:
        for dr,dc in [(0,0),(-1,0),(1,0),(0,-1),(0,1)]:
            out[r+dr][c+dc]=3
    return out