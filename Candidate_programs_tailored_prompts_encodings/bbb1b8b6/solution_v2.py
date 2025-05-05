def solve(grid):
    H = len(grid)
    W = len(grid[0]) if H else 0
    divider = None
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 5:
                divider = c
                break
        if divider is not None:
            break
    left_w = divider
    right_start = divider + 1
    blue = set()
    for r in range(H):
        for c in range(left_w):
            if grid[r][c] == 1:
                blue.add((r, c))
    colored = []
    for r in range(H):
        for c in range(right_start, W):
            v = grid[r][c]
            if v not in (0, 5, 1):
                colored.append((r, c - right_start, v))
    if any((r, cc) in blue for r, cc, _ in colored):
        colored = []
    out = [[0] * left_w for _ in range(H)]
    for r, cc, v in colored:
        out[r][cc] = v
    for r, c in blue:
        out[r][c] = 1
    return out