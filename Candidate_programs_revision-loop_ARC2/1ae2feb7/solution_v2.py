from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    c = next(j for j in range(w) if all(grid[i][j] == 2 for i in range(h)))
    out = [row[:] for row in grid]
    for r in range(h):
        v = None
        j = c - 1
        while j >= 0:
            if grid[r][j] not in (0, 2):
                v = grid[r][j]
                break
            j -= 1
        if v is None:
            continue
        k = j
        while k >= 0 and grid[r][k] == v:
            k -= 1
        block = j - k
        for i in range(c + 1, w):
            if (i - c - 1) % block == 0:
                out[r][i] = v
            else:
                out[r][i] = 0
    return out