def solve(grid):
    m, n = len(grid), len(grid[0])
    freq = {}
    for row in grid:
        for v in row:
            freq[v] = freq.get(v, 0) + 1
    bg = max(freq, key=lambda k: freq[k])
    color_groups = {}
    min_row = {}
    for i in range(m):
        for j in range(n):
            v = grid[i][j]
            if v != bg:
                color_groups.setdefault(v, []).append((i, j))
                if v not in min_row or i < min_row[v]:
                    min_row[v] = i
    colors = sorted(color_groups.keys(), key=lambda c: min_row[c])
    out = [[bg] * n for _ in range(m)]
    for idx, c in enumerate(colors):
        shift = -1 if idx % 2 == 0 else 1
        for i, j in color_groups[c]:
            out[i][j + shift] = c
    return out