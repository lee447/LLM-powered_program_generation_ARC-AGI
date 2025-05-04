from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v in (2, 3, 4, 6):
                size = 2 if v in (2, 4) else 3
                sr = r - size // 2
                sc = c - size // 2
                for dr in range(size):
                    for dc in range(size):
                        rr, cc = sr + dr, sc + dc
                        if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] != 0:
                            out[rr][cc] = v
    return out