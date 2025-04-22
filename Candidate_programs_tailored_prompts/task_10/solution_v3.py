def solve(grid):
    h = len(grid)
    w = len(grid[0])
    anchors = []
    for r in range(h):
        c = 0
        while c <= w-3:
            if grid[r][c] == 2 and grid[r][c+1] == 2 and grid[r][c+2] == 2:
                anchors.append((r, c))
                c += 3
            else:
                c += 1
    if not anchors:
        return [row[:] for row in grid]
    stripe = None
    for r in range(h):
        if all(grid[r][c] == 0 for c in range(w)):
            stripe = r
            break
    if stripe is None:
        stripe = h // 2
    # choose the anchor whose span of three best fits in bounds
    anchors.sort(key=lambda x: abs(x[0] - stripe))
    _, ac = anchors[0]
    out = [row[:] for row in grid]
    for dc in range(3):
        out[stripe][ac + dc] = 8
    return out