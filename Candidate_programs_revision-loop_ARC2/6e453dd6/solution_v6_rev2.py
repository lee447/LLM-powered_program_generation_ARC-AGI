from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    div = next(c for c in range(w) if all(grid[r][c] == 5 for r in range(h)))
    left = range(div)
    right = range(div + 1, w)
    cnts = [sum(1 for c in left if grid[r][c] == 0) for r in range(h)]
    freq = {}
    for v in cnts:
        if v > 0:
            freq[v] = freq.get(v, 0) + 1
    if not freq:
        return grid
    target = max(freq.items(), key=lambda x: x[1])[0]
    out = [row[:] for row in grid]
    for r in range(h):
        if cnts[r] != target:
            for c in right:
                if out[r][c] == 2:
                    out[r][c] = 6
    return out