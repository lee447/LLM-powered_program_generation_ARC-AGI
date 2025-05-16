def solve(grid):
    h, w = len(grid), len(grid[0])
    border = grid[0][0]
    brs = [r for r in range(h) if all(grid[r][c] == border for c in range(w))]
    bcs = [c for c in range(w) if all(grid[r][c] == border for r in range(h))]
    rows, cols = len(brs) - 1, len(bcs) - 1
    def get_pattern(i, j):
        return [
            tuple(grid[r][c] for c in range(bcs[j] + 1, bcs[j+1]))
            for r in range(brs[i] + 1, brs[i+1])
        ]
    base = [get_pattern(0, j) for j in range(cols)]
    changed = [None] * cols
    for j in range(cols):
        for i in range(1, rows):
            p = get_pattern(i, j)
            if p != base[j]:
                changed[j] = (p, i)
                break
    out = [row[:] for row in grid]
    for j in range(cols):
        if changed[j]:
            p, i = changed[j]
            for di, r in enumerate(range(brs[i] + 1, brs[i+1])):
                for dj, c in enumerate(range(bcs[j] + 1, bcs[j+1])):
                    out[r][c] = p[di][dj]
    return out