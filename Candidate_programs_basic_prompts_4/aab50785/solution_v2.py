def solve(grid):
    blocks = {}
    h = len(grid)
    w = len(grid[0])
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j]==8 and grid[i][j+1]==8 and grid[i+1][j]==8 and grid[i+1][j+1]==8:
                blocks.setdefault(i, []).append(j)
    out = []
    for i in sorted(blocks):
        js = sorted(blocks[i])
        j1, j2 = js[0], js[1]
        for r in (i, i+1):
            out.append([grid[r][c] for c in range(j1+2, j2)])
    return out