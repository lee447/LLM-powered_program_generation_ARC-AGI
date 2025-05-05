def solve(grid):
    h=len(grid);w=len(grid[0])
    pts=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==2]
    (r1,c1),(r2,c2)=pts
    dr=(r2>r1)-(r2<r1);dc=(c2>c1)-(c2< c1)
    path=[];r,c=r1,c1
    while True:
        path.append((r,c))
        if (r,c)==(r2,c2):break
        r+=dr;c+=dc
    out=[row[:] for row in grid]
    for i,(r,c) in enumerate(path):
        if i!=0 and i!=len(path)-1:
            out[r][c]=2 if i%2 else 3
    return out