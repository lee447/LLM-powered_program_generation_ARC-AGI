def solve(grid):
    H = len(grid)
    W = len(grid[0])
    for r in range(H):
        if all(grid[r][c] == 0 for c in range(W)):
            if 0 < r < H-1 and any(grid[r-1][c] != 0 for c in range(W)) and any(grid[r+1][c] != 0 for c in range(W)):
                for c in range(W):
                    grid[r][c] = 3
                return grid
    for c in range(W):
        if all(grid[r][c] == 0 for r in range(H)):
            if 0 < c < W-1 and any(grid[r][c-1] != 0 for r in range(H)) and any(grid[r][c+1] != 0 for r in range(H)):
                for r in range(H):
                    grid[r][c] = 3
                return grid
    return grid