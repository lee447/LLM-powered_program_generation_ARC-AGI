from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    original = [row[:] for row in grid]
    output = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if original[r][c] == 1:
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < h and 0 <= nc < w and original[nr][nc] == 0:
                            output[nr][nc] = 1
    return output