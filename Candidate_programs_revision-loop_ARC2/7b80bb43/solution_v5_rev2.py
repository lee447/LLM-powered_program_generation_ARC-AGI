from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    freq = {}
    for y in range(h):
        for x in range(w):
            freq[grid[y][x]] = freq.get(grid[y][x], 0) + 1
    bg = max(freq, key=lambda c: freq[c])
    tgt = next(c for c in freq if c != bg)
    segs_by_row = {}
    for y in range(h):
        segs = []
        x = 0
        while x < w:
            if grid[y][x] == tgt:
                a = x
                while x < w and grid[y][x] == tgt:
                    x += 1
                segs.append((a, x - 1))
            else:
                x += 1
        if len(segs) == 2:
            segs_by_row[y] = sorted(segs)
    segs_by_col = {}
    for x in range(w):
        segs = []
        y = 0
        while y < h:
            if grid[y][x] == tgt:
                a = y
                while y < h and grid[y][x] == tgt:
                    y += 1
                segs.append((a, y - 1))
            else:
                y += 1
        if len(segs) == 2:
            segs_by_col[x] = sorted(segs)
    if segs_by_col:
        x, (a0, b0), (a1, b1) = next(iter(segs_by_col.items()))[0], *next(iter(segs_by_col.values()))
        for y in range(b0 + 1, a1):
            grid[y][x] = tgt
    if segs_by_row:
        y, ((a0, b0), (a1, b1)) = next(iter(segs_by_row.items()))
        for x in range(b0 + 1, a1):
            grid[y][x] = tgt
    return grid