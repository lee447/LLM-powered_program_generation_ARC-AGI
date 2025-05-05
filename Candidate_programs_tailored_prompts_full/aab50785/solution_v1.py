def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    sections = []
    for r in range(h - 1):
        cs = []
        for c in range(w - 1):
            if grid[r][c] == 8 and grid[r][c+1] == 8 and grid[r+1][c] == 8 and grid[r+1][c+1] == 8:
                cs.append(c)
        if len(cs) == 2:
            cs.sort()
            sections.append((r, cs[0], cs[1]))
    out = []
    for r, c0, c1 in sections:
        start = c0 + 2
        end = c1
        out.append([grid[r][c] for c in range(start, end)])
        out.append([grid[r+1][c] for c in range(start, end)])
    return out