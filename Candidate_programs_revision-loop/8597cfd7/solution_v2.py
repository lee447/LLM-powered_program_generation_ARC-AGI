from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    stripe = next(i for i, row in enumerate(grid) if row.count(5) > n//2)
    above_counts, below_counts = {}, {}
    for i in range(stripe):
        for v in grid[i]:
            if v not in (0,5):
                above_counts[v] = above_counts.get(v, 0) + 1
    for i in range(stripe+1, m):
        for v in grid[i]:
            if v not in (0,5):
                below_counts[v] = below_counts.get(v, 0) + 1
    colors = set(above_counts) | set(below_counts)
    best = min(colors, key=lambda c: (-abs(above_counts.get(c,0)-below_counts.get(c,0)), c))
    return [[best, best], [best, best]]