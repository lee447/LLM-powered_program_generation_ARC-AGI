def solve(grid):
    h = len(grid)
    w = len(grid[0])
    blocks = []
    for r in range(h - 1):
        for c in range(w - 1):
            if grid[r][c] == grid[r][c+1] == grid[r+1][c] == grid[r+1][c+1] == 2:
                blocks.append((c, r))
    blocks.sort(key=lambda x: (x[0], x[1]))
    n = len(blocks)
    start = 0 if n % 2 == 1 else 1
    for i in range(start, n, 2):
        c, r = blocks[i]
        grid[r][c] = 8
        grid[r][c+1] = 8
        grid[r+1][c] = 8
        grid[r+1][c+1] = 8
    return grid