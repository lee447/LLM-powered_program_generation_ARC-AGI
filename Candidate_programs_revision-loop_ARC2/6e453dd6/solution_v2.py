def solve(grid):
    h = len(grid)
    w = len(grid[0])
    div = next(c for c in range(w) if all(grid[r][c] == 5 for r in range(h)))
    left_w = div
    cnts = [sum(1 for c in range(div) if grid[r][c] == 0) for r in range(h)]
    freq = {}
    for c in cnts:
        freq[c] = freq.get(c, 0) + 1
    target = next(c for c in sorted(set(cnts)) if c > 0 and freq[c] > 1)
    out = [row[:] for row in grid]
    for r in range(h):
        if cnts[r] == target:
            for c in range(div + 1, w):
                out[r][c] = 2
    return out