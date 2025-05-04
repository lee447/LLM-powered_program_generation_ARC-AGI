from typing import List
from collections import Counter

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    zeros = [(y, x) for y in range(h) for x in range(w) if grid[y][x] == 0]
    ctr1 = Counter(x - y for y, x in zeros)
    ctr2 = Counter(x + y for y, x in zeros)
    k1, m1 = ctr1.most_common(1)[0]
    k2, m2 = ctr2.most_common(1)[0]
    slope = 1 if m1 >= m2 else -1
    k = k1 if slope == 1 else k2
    out = [row[:] for row in grid]
    for y in range(h):
        x = y + k if slope == 1 else k - y
        if 0 <= x < w and grid[y][x] == 0:
            out[y][x] = 8
    return out