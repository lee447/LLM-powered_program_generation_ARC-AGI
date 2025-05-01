def solve(grid):
    eights=[(i,j)for i in range(len(grid))for j in range(len(grid[0]))if grid[i][j]==8]
    if not eights:return[]
    rs=[i for i,j in eights];cs=[j for i,j in eights]
    r0,r1=min(rs),max(rs)
    c0,c1=min(cs),max(cs)
    n=r1-r0+1
    start=c0-n
    return [grid[r][start:c0] for r in range(r0,r0+n)]