from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    color = next(cell for row in grid for cell in row if cell != 0)
    pattern = [[color if grid[i][j] == 0 else 0 for j in range(w)] for i in range(h)]
    out = [[0] * (w * w) for _ in range(h * h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 0:
                for u in range(h):
                    for v in range(w):
                        out[i*h + u][j*w + v] = pattern[u][v]
    return out