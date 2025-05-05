def solve(grid):
    H, W = len(grid), len(grid[0])
    row_seps = [r for r in range(H) if all(grid[r][c] == grid[r][0] for c in range(1, W))]
    col_seps = [c for c in range(W) if all(grid[r][c] == grid[0][c] for r in range(1, H))]
    row_bounds = [-1] + sorted(row_seps) + [H]
    col_bounds = [-1] + sorted(col_seps) + [W]
    row_bands = [(row_bounds[i] + 1, row_bounds[i+1] - 1) for i in range(len(row_bounds)-1) if row_bounds[i] + 1 <= row_bounds[i+1] - 1]
    col_bands = [(col_bounds[j] + 1, col_bounds[j+1] - 1) for j in range(len(col_bounds)-1) if col_bounds[j] + 1 <= col_bounds[j+1] - 1]
    return [[grid[rb[0]][cb[0]] for cb in col_bands] for rb in row_bands]