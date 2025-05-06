from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    c = next((v for row in grid for v in row if v != 0), 0)
    ys = [i for i in range(h) for j in range(w) if grid[i][j] == c]
    xs = [j for i in range(h) for j in range(w) if grid[i][j] == c]
    if not ys or not xs:
        return [[0]*w for _ in range(h)]
    min_y, max_y = min(ys), max(ys)
    min_x, max_x = min(xs), max(xs)
    pat = [-1, 0, 1, 0]
    out = [[0]*w for _ in range(h)]
    for i in range(h):
        if i == min_y or i == max_y:
            dx = 0
        else:
            ro = i - min_y
            dx = pat[(ro-1) % 4]
        for j in range(w):
            if grid[i][j] == c:
                out[i][j+dx] = c
    return out