def solve(grid):
    h,len0=len(grid),len(grid[0])
    fives=[(r,c)for r in range(h)for c in range(len0)if grid[r][c]==5]
    fives.sort()
    (sr,sc),(dr,dc)=fives[0],fives[-1]
    templ=[(r-sr,c-sc,grid[r][c])for r in range(h)for c in range(len0)if grid[r][c]!=0 and not(r==sr and c==sc)]
    out=[row[:]for row in grid]
    for dy,dx,color in templ:
        y, x = dr+dy, dc+dx
        if 0<=y<h and 0<=x<len0:
            out[y][x]=color
    return out