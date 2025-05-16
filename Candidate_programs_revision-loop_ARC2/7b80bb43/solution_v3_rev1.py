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
        segs_by_row[y] = segs
    rows2 = [y for y, segs in segs_by_row.items() if len(segs) == 2]
    if len(rows2) != 1:
        return grid
    y = rows2[0]
    segs = sorted(segs_by_row[y], key=lambda s: s[0])
    (a0, b0), (a1, b1) = segs
    for x in range(b0 + 1, a1):
        grid[y][x] = tgt
    return grid