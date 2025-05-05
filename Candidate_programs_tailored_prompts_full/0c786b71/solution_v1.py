def solve(grid):
    h = len(grid)
    patterns = [row[::-1] + row for row in grid]
    out = []
    mh = 2*h - 1
    for r in range(2*h):
        i = min(r, mh - r)
        out.append(patterns[h-1 - i])
    return out