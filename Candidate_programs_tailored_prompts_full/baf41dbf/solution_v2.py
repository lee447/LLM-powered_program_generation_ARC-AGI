def solve(grid):
    h = len(grid)
    w = len(grid[0])
    anchors = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 6]
    border = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 3]
    min_r = min(r for r, _ in border)
    max_r = max(r for r, _ in border)
    min_c = min(c for _, c in border)
    max_c = max(c for _, c in border)
    above = [r for r, _ in anchors if r < min_r]
    below = [r for r, _ in anchors if r > max_r]
    left  = [c for _, c in anchors if c < min_c]
    right = [c for _, c in anchors if c > max_c]
    expand_up = (min_r - max(above) - 1) if above else 0
    expand_down = (min(below) - max_r - 1) if below else 0
    expand_left = (min_c - max(left) - 1) if left else 0
    expand_right = (min(right) - max_c - 1) if right else 0
    new_min_r = min_r - expand_up
    new_max_r = max_r + expand_down
    new_min_c = min_c - expand_left
    new_max_c = max_c + expand_right
    out = [row[:] for row in grid]
    for r, c in border:
        out[r][c] = 0
    for c in range(new_min_c, new_max_c + 1):
        out[new_min_r][c] = 3
        out[new_max_r][c] = 3
    for r in range(new_min_r, new_max_r + 1):
        out[r][new_min_c] = 3
        out[r][new_max_c] = 3
    return out