import copy
def solve(grid):
    h=len(grid)
    w=len(grid[0]) if h else 0
    out=[row[:] for row in grid]
    template=None
    tc=None
    for r in range(1,h-1):
        for c in range(1,w-1):
            if grid[r][c]==8:
                vals=[grid[r+dr][c+dc] for dr in (-1,0,1) for dc in (-1,0,1)]
                if 0 not in vals and vals.count(8)==1:
                    template=[[grid[r+dr][c+dc] for dc in (-1,0,1)] for dr in (-1,0,1)]
                    tc=(r,c)
                    break
        if template: break
    if not template:
        return out
    for r in range(1,h-1):
        for c in range(1,w-1):
            if grid[r][c]==8 and (r,c)!=tc:
                ok=True
                for i in range(3):
                    for j in range(3):
                        t=template[i][j]
                        gi=grid[r+i-1][c+j-1]
                        if t==1 and gi!=1: ok=False; break
                        if t==8 and not (i==1 and j==1): ok=False; break
                    if not ok: break
                if not ok: continue
                for i in range(3):
                    for j in range(3):
                        if template[i][j]==4 and grid[r+i-1][c+j-1]==0:
                            out[r+i-1][c+j-1]=4
    return out