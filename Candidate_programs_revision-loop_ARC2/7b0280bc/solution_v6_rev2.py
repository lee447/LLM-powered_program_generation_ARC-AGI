from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    positions = {}
    for i in range(h - 1):
        for j in range(w - 1):
            c = grid[i][j]
            if c != bg and grid[i][j+1] == c and grid[i+1][j] == c and grid[i+1][j+1] == c:
                positions.setdefault(c, []).append((i, j))
    if not positions:
        return grid
    c_max = max(positions.keys(), key=lambda c: len(positions[c]))
    pos = positions[c_max]
    k = len(pos)
    if k <= 2:
        return grid
    fill = 5 if c_max % 2 == 0 else 3
    count = k if c_max % 2 == 0 else k // 2
    out = [row[:] for row in grid]
    for i, j in pos[:count]:
        out[i][j] = fill
        out[i][j+1] = fill
        out[i+1][j] = fill
        out[i+1][j+1] = fill
    return out