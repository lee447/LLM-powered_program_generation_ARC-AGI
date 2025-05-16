from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    div = next(c for c in range(w) if all(grid[r][c] == 5 for r in range(h)))
    left_w = div
    cnts = [sum(1 for c in range(left_w) if grid[r][c] == 0) for r in range(h)]
    freq = {}
    for v in cnts:
        freq[v] = freq.get(v, 0) + 1
    target = max((v for v in freq if v > 0 and freq[v] > 1), key=lambda v: freq[v])
    out = [row[:] for row in grid]
    for r in range(h):
        if cnts[r] == target:
            for c in range(div + 1, w):
                out[r][c] = 2
    return out