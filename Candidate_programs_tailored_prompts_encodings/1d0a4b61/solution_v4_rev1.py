from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    border = grid[0][0]
    b1 = next(i for i in range(1, h) if all(v == border for v in grid[i]))
    block = grid[1:b1]
    bh = len(block)
    out = [row[:] for row in grid]
    bands = []
    r = 0
    while r < h:
        if any(v == 0 for v in grid[r]):
            s = r
            while r+1 < h and any(v == 0 for v in grid[r+1]):
                r += 1
            bands.append((s, r))
        r += 1
    for k, (s, e) in enumerate(bands):
        for r in range(s, e+1):
            i = r - s
            for c in range(w):
                if grid[r][c] == 0:
                    out[r][c] = block[(i + k) % bh][c]
    return out