from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    blocks = [(r, c) for r in range(h-1) for c in range(w-1)
              if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2]
    cols = sorted({c for r, c in blocks})
    mid = (w-1)/2
    evens = [c for i, c in enumerate(cols) if i%2==0]
    odds  = [c for i, c in enumerate(cols) if i%2==1]
    def score(lst):
        return abs((sum(lst)/len(lst) if lst else float('inf')) - mid)
    sel = evens if score(evens) <= score(odds) else odds
    rows_by_col = {}
    for r,c in blocks:
        rows_by_col.setdefault(c, []).append(r)
    out = [row[:] for row in grid]
    for c in sel:
        rs = sorted(rows_by_col.get(c, []))
        s = set(rs)
        for r in rs:
            if r+1 in s:
                out[r][c]=out[r][c+1]=out[r+1][c]=out[r+1][c+1]=8
    return out