def solve(grid):
    H, W = len(grid), len(grid[0])
    anchors = []
    for r in range(H-1):
        for c in range(W-1):
            if grid[r][c] == 2 and grid[r][c+1] == 2 and grid[r+1][c] == 2 and grid[r+1][c+1] == 2:
                anchors.append((r, c))
    anchors.sort(key=lambda x: (x[0], x[1]))
    out = [row[:] for row in grid]
    for i, (r, c) in enumerate(anchors):
        if i % 2 == 0:
            for dr in (0, 1):
                for dc in (0, 1):
                    out[r+dr][c+dc] = 8
    return out