def solve(grid):
    H, W = len(grid), len(grid[0])
    anchors = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == 4]
    clusters = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == 2]
    origin = min(anchors, key=lambda a: max(max(abs(i - a[0]), abs(j - a[1])) for i, j in clusters))
    offsets = [(i - origin[0], j - origin[1]) for i, j in clusters]
    out = [[0] * W for _ in range(H)]
    for i, j in anchors:
        out[i][j] = 4
    for i0, j0 in anchors:
        for dr, dc in offsets:
            i, j = i0 + dr, j0 + dc
            if 0 <= i < H and 0 <= j < W and out[i][j] != 4:
                out[i][j] = 2
    return out