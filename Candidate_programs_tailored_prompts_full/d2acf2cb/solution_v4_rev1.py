from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h=len(grid); w=len(grid[0])
    out=[row[:] for row in grid]
    hr=[]
    for r in range(h):
        cols=[c for c in range(w) if grid[r][c]==4]
        if len(cols)>=2:
            cols.sort()
            hr.append((r,cols[0],cols[-1]))
    hc=[]
    for c in range(w):
        rows=[r for r in range(h) if grid[r][c]==4]
        if len(rows)>=2:
            rows.sort()
            hc.append((c,rows[0],rows[-1]))
    if len(hr)>len(hc):
        m=(8,7) if len(hr)==1 else (6,0)
        for r,c1,c2 in hr:
            iv=sorted({grid[r][c] for c in range(c1+1,c2)})
            mp={iv[i]:m[i] for i in range(len(iv))}
            for c in range(c1+1,c2):
                out[r][c]=mp.get(grid[r][c],out[r][c])
    else:
        m=(8,7)
        for c,r1,r2 in hc:
            iv=sorted({grid[r][c] for r in range(r1+1,r2)})
            mp={iv[i]:m[i] for i in range(len(iv))}
            for r in range(r1+1,r2):
                out[r][c]=mp.get(grid[r][c],out[r][c])
    return out