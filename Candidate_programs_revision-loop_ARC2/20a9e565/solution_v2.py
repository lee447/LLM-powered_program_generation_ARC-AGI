def solve(grid):
    from collections import deque
    h, w = len(grid), len(grid[0])
    color_counts = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v != 0:
                color_counts[v] = color_counts.get(v, 0) + 1
    target = max(color_counts, key=lambda c: color_counts[c])
    rows = [i for i in range(h) for j in range(w) if grid[i][j] == target]
    cols = [j for i in range(h) for j in range(w) if grid[i][j] == target]
    r0, r1 = min(rows), max(rows)
    c0, c1 = min(cols), max(cols)
    out = []
    for i in range(r0, r1+1):
        row = []
        for j in range(c0, c1+1):
            row.append(grid[i][j] if grid[i][j] == target else 0)
        out.append(row)
    return out