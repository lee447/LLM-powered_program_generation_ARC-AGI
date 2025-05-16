from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    centers = []
    for r in range(h):
        for c in range(1, w-1):
            if grid[r][c] == 7 and grid[r][c-1] == 7 and grid[r][c+1] == 7:
                centers.append((r, c))
    out = [[0]*w for _ in range(h)]
    for r in range(h):
        if any(grid[r][c] == 7 for c in range(w)):
            for c in range(w):
                if grid[r][c] == 0:
                    out[r][c] = 0
                elif grid[r][c] == 7:
                    out[r][c] = 8
        else:
            stripe = 2 if r % 4 == 2 else 0
            for c in range(w):
                if grid[r][c] == 0:
                    out[r][c] = 0
                elif stripe and (c < stripe or c >= w - stripe):
                    out[r][c] = 3
                else:
                    out[r][c] = 8
    for r, c in centers:
        for dr in (-1, 0, 1):
            rr = r + dr
            if 0 <= rr < h:
                out[rr][c] = 6
    return out