from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for r in range(H):
        sixes = [c for c,v in enumerate(grid[r]) if v==6]
        if not sixes: continue
        s,e = sixes[0], sixes[-1]
        greens = [c for c,v in enumerate(grid[r]) if v==3]
        L = max(c for c in greens if c<s)
        R = min(c for c in greens if c>e)
        arr = [grid[r][c] for c in range(L+1,R) if grid[r][c]!=6]
        for i,c in enumerate(sixes):
            out[r][c] = arr[-1-i]
    return out