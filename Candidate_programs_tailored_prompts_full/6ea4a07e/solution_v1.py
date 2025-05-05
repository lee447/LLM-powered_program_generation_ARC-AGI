def solve(grid):
    mapping = {8: 2, 3: 1, 5: 4}
    h = len(grid)
    w = len(grid[0]) if h else 0
    color = next((grid[i][j] for i in range(h) for j in range(w) if grid[i][j] != 0), 0)
    fill = mapping.get(color, 0)
    output = [[fill for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0:
                output[i][j] = 0
    return output