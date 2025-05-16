from typing import List
from collections import Counter

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    cnt = Counter(c for row in grid for c in row)
    bg, _ = cnt.most_common(1)[0]
    pts = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] != bg]
    if not pts:
        return []
    r0 = min(r for r, _ in pts)
    r1 = max(r for r, _ in pts)
    c0 = min(c for _, c in pts)
    c1 = max(c for _, c in pts)
    H, W = r1 - r0 + 1, c1 - c0 + 1
    if H == 2*(((H+1)//2)) - 1 and W == 2*(((W+1)//2)) - 1:
        th = (H+1)//2
        tw = (W+1)//2
        return [row[c0:c0+tw] for row in grid[r0:r0+th]]
    return [row[c0:c0+W] for row in grid[r0:r0+H]]