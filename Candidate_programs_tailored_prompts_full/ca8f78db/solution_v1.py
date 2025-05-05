def solve(grid):
    h = len(grid)
    w = len(grid[0])
    stripe_rows = [r for r in range(h) if any(cell > 1 for cell in grid[r])]
    base_row = next(r for r in stripe_rows if all(cell != 0 for cell in grid[r][1:-1]))
    content = grid[base_row][1:-1]
    L = next(L for L in range(1, len(content)+1) if all(content[i] == content[i % L] for i in range(len(content))))
    cycle = content[:L]
    result = [row[:] for row in grid]
    for r in range(h):
        if r in stripe_rows:
            for c in range(1, w-1):
                if grid[r][c] == 0:
                    result[r][c] = cycle[(c-1) % L]
        else:
            for c in range(1, w-1):
                if grid[r][c] == 0:
                    result[r][c] = 1
    return result