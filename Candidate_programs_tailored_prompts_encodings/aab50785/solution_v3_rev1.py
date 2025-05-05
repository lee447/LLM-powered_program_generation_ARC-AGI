import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    out = []
    for r in range(h-1):
        cs = [c for c in range(w-1) if grid[r][c]==8 and grid[r][c+1]==8 and grid[r+1][c]==8 and grid[r+1][c+1]==8]
        if len(cs)==2:
            c1, c2 = sorted(cs)
            for rr in (r, r+1):
                row = []
                for cc in range(c1+2, c2):
                    v = grid[rr][cc]
                    row.append(0 if v==8 else v)
                out.append(row)
    return out