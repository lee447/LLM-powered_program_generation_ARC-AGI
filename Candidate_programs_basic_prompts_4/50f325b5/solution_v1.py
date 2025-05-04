def solve(grid):
    n=len(grid);m=len(grid[0])
    coords=[(i,j)for i in range(n)for j in range(m)if grid[i][j]==8]
    minr=min(i for i,j in coords);minc=min(j for i,j in coords)
    offsets=[(i-minr,j-minc)for i,j in coords]
    h=max(i-minr for i,j in coords)+1;w=max(j-minc for i,j in coords)+1
    rots=[];dims=[]
    offs=offsets;hh,ww=h,w
    for _ in range(4):
        rots.append(offs);dims.append((hh,ww))
        offs=[(dy,hh-1-dx)for dx,dy in offs]
        hh,ww=ww,hh
    orig=grid
    out=[row[:]for row in grid]
    for k in range(4):
        offs=rots[k];hh,ww=dims[k]
        for i in range(n-hh+1):
            for j in range(m-ww+1):
                dx0,dy0=offs[0];C=orig[i+dx0][j+dy0]
                if C==0 or C==8:continue
                ok=True
                for dx,dy in offs:
                    if orig[i+dx][j+dy]!=C:
                        ok=False;break
                if not ok:continue
                for dx,dy in offs:
                    out[i+dx][j+dy]=8
    return out