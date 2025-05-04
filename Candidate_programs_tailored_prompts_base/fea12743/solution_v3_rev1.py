from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    shapes = []
    for r in range(h - 3):
        for c in range(w - 3):
            if all(grid[r][c + i] != 0 and grid[r + 3][c + i] != 0 and grid[r + i][c] != 0 and grid[r + i][c + 3] != 0 for i in range(4)):
                shapes.append((r, c))
    shapes.sort()
    rows = sorted({r for r, _ in shapes})
    tiers = [[(r, c) for r0, c in shapes if r0 == r] for r in rows]
    palette = [2, 8, 3]
    res = [row[:] for row in grid]
    for ti, tier in enumerate(tiers):
        for j, (r0, c0) in enumerate(tier):
            col = palette[(ti + j) % len(palette)]
            for dr in range(4):
                for dc in range(4):
                    if grid[r0 + dr][c0 + dc] != 0:
                        res[r0 + dr][c0 + dc] = col
    return res