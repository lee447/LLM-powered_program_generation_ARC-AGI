def solve(grid):
    h=len(grid)
    w=len(grid[0]) if h else 0
    out=[row[:] for row in grid]
    for r in range(h-2):
        for c in range(w-2):
            has1=False
            has8=False
            for i in range(3):
                for j in range(3):
                    v=grid[r+i][c+j]
                    if v==1: has1=True
                    if v==8: has8=True
            if has1 and has8:
                for i in range(3):
                    for j in range(3):
                        if grid[r+i][c+j]==0:
                            out[r+i][c+j]=4
    return out