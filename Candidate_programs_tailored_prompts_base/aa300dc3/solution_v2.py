from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    interior = list(range(1, h-1))
    zero_cols = {y: [x for x in range(w) if grid[y][x] == 0] for y in interior}
    first, second = interior[0], interior[1]
    min1, max1 = min(zero_cols[first]), max(zero_cols[first])
    min2 = min(zero_cols[second])
    descending = min2 < min1
    x = max1 if descending else min1
    for i, y in enumerate(interior):
        if i > 0:
            x = x - 1 if descending else x + 1
        zs = zero_cols[y]
        if not zs:
            continue
        lo, hi = min(zs), max(zs)
        if x < lo:
            x = lo
        elif x > hi:
            x = hi
        elif grid[y][x] != 0:
            for d in range(1, w):
                left, right = x - d, x + d
                okl = left >= lo and left in zs
                okr = right <= hi and right in zs
                if okl or okr:
                    if okl:
                        x = left
                    else:
                        x = right
                    break
        out[y][x] = 8
    return out