from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    row7 = [r.count(7) for r in grid]
    M = max(row7)
    top = next(i for i, c in enumerate(row7) if c == M)
    bottom = len(row7) - 1 - row7[::-1].index(M)
    runs = []
    i = 0
    while i < W:
        if grid[top][i] == 7:
            j = i
            while j < W and grid[top][j] == 7:
                j += 1
            runs.append((i, j - 1))
            i = j
        else:
            i += 1
    runs.sort(key=lambda x: x[1] - x[0], reverse=True)
    left, right = runs[0]
    col6 = [sum(grid[y][x] == 6 for y in range(H)) for x in range(W)]
    pinks = [x for x, c in enumerate(col6) if c > H // 4]
    if not pinks:
        return grid
    ps, pe = pinks[0], pinks[-1]
    x0, x1 = left + 1, right - 1
    out = [row[:] for row in grid]
    for y in range(top + 1, bottom):
        segs = []
        x = x0
        while x <= x1:
            if grid[y][x] in (1, 2, 3, 4):
                a = x
                while x <= x1 and grid[y][x] in (1, 2, 3, 4):
                    x += 1
                segs.append((a, x - 1))
            else:
                x += 1
        if segs:
            a, b = segs[0]
            vals = [grid[y][k] for k in range(a, b + 1)][::-1]
            for i, v in enumerate(vals):
                if ps + i <= pe:
                    out[y][ps + i] = v
    return out