from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h > 0 else 0
    output = [row[:] for row in grid]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 1:
                for dr, dc in directions:
                    ok = True
                    for k in (1, 2, 3):
                        nr = r + dr * k
                        nc = c + dc * k
                        if not (0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 0):
                            ok = False
                            break
                    if ok:
                        for k in (1, 2, 3):
                            output[r + dr * k][c + dc * k] = 1
    return output