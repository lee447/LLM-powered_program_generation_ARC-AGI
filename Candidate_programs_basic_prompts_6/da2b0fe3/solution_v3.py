def solve(grid):
    n=len(grid); m=len(grid[0])
    coords=[(i,j) for i in range(n) for j in range(m) if grid[i][j]!=0]
    if not coords: return [row[:] for row in grid]
    rs=[i for i,j in coords]; cs=[j for i,j in coords]
    h=max(rs)-min(rs)+1; w=max(cs)-min(cs)+1
    out=[row[:] for row in grid]
    mid_r=(n-1)//2; mid_c=(m-1)//2
    if h>w:
        for j in range(m): out[mid_r][j]=3
    else:
        for i in range(n): out[i][mid_c]=3
    return out