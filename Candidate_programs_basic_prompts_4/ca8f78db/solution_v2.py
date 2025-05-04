def solve(grid):
    h=len(grid);w=len(grid[0])
    stripe=grid[0][0]
    tile_row=None
    for i in range(1,h,2):
        r=grid[i]
        if 0 not in r and len(set(r))>1:
            tile_row=r
            break
    k=1
    while k<=w:
        ok=True
        for j in range(w):
            if tile_row[j]!=tile_row[j%k]:
                ok=False;break
        if ok:break
        k+=1
    tile=tile_row[:k]
    out=[]
    for i in range(h):
        if i%2==0:
            out.append([stripe]*w)
        else:
            row=[tile[j%k] for j in range(w)]
            out.append(row)
    return out