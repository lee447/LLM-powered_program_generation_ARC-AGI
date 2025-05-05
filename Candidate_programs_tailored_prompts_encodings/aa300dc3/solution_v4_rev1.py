from typing import List
from collections import defaultdict

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    counts = defaultdict(set)
    for r in range(1, h-1):
        for c, v in enumerate(grid[r]):
            if v == 0:
                for s in (1, -1):
                    d = c - s * r
                    counts[(s, d)].add(r)
    best_key, best_rows = None, set()
    for key, rows in counts.items():
        if len(rows) > len(best_rows):
            best_key, best_rows = key, rows
    s, d = best_key
    res = [row[:] for row in grid]
    for r in best_rows:
        c = s * r + d
        res[r][c] = 8
    return res