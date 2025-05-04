def solve(grid):
    R, C = len(grid), len(grid[0])
    key = [(r, c) for r in range(R) for c in range(C) if grid[r][c] > 1]
    min_r = min(r for r, _ in key)
    max_r = max(r for r, _ in key)
    min_c = min(c for _, c in key)
    max_c = max(c for _, c in key)
    h, w = max_r - min_r + 1, max_c - min_c + 1
    pattern = {}
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            v = grid[r][c]
            if v > 1:
                pattern[(r - min_r, c - min_c)] = v
    shapes = []
    for i in range(R - h + 1):
        for j in range(C - w + 1):
            if all(grid[i + dr][j + dc] == 1 for dr, dc in pattern):
                shapes.append((i, j))
    shapes.sort()
    out = [row[:] for row in grid]
    for i, j in shapes:
        for (dr, dc), v in pattern.items():
            out[i + dr][j + dc] = v
    return out