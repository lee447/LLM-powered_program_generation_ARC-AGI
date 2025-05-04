from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    seeds = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    for r, c in seeds:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 0:
                    out[nr][nc] = 1
    return out