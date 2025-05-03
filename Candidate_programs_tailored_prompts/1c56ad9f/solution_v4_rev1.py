from typing import List
import math

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    nonzero = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0]
    if not nonzero:
        return grid
    minr = min(r for r, _ in nonzero)
    maxr = max(r for r, _ in nonzero)
    runs = sorted({sum(1 for c in range(w) if grid[r][c] != 0) for r in range(minr, maxr+1)})
    if len(runs) >= 2 and runs[0] > 0:
        amp = runs[1] // runs[0]
    else:
        amp = 1
    length = maxr - minr if maxr > minr else 1
    out = [[0]*w for _ in range(h)]
    for r, c in nonzero:
        phase = (r - minr) / length * 2 * math.pi
        shift = int(round(math.sin(phase) * amp))
        nc = c + shift
        if 0 <= nc < w:
            out[r][nc] = grid[r][c]
    return out