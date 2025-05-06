def solve(grid):
    h, w = len(grid), len(grid[0])
    freq = {}
    for row in grid:
        for c in row:
            freq[c] = freq.get(c, 0) + 1
    bg = max(freq, key=lambda c: freq[c])
    ys = [y for y in range(h) for x in range(w) if grid[y][x] != bg]
    xs = [x for y in range(h) for x in range(w) if grid[y][x] != bg]
    if not ys or not xs:
        return []
    y0, y1 = min(ys), max(ys)
    x0, x1 = min(xs), max(xs)
    return [row[x0:x1+1] for row in grid[y0:y1+1]]