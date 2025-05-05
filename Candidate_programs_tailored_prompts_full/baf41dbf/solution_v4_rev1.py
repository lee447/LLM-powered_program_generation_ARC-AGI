from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    anchors = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 6]
    border_cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 3]
    rs = [r for r, _ in border_cells]
    cs = [c for _, c in border_cells]
    min_r, max_r = min(rs), max(rs)
    min_c, max_c = min(cs), max(cs)
    c_divs = [c for c in range(min_c + 1, max_c) if all(grid[r][c] == 3 for r in range(min_r + 1, max_r))]
    above = [r for r, _ in anchors if r < min_r]
    below = [r for r, _ in anchors if r > max_r]
    left = [c for _, c in anchors if c < min_c]
    right = [c for _, c in anchors if c > max_c]
    expand_up = (min_r - max(above) - 1) if above else 0
    expand_down = (min(below) - max_r - 1) if below else 0
    expand_left = (min_c - max(left) - 1) if left else 0
    expand_right = (min(right) - max_c - 1) if right else 0
    new_min_r, new_max_r = min_r - expand_up, max_r + expand_down
    new_min_c, new_max_c = min_c - expand_left, max_c + expand_right
    out = [row[:] for row in grid]
    for r, c in border_cells:
        out[r][c] = 0
    for c in range(new_min_c, new_max_c + 1):
        if out[new_min_r][c] != 6: out[new_min_r][c] = 3
        if out[new_max_r][c] != 6: out[new_max_r][c] = 3
    for r in range(new_min_r, new_max_r + 1):
        if out[r][new_min_c] != 6: out[r][new_min_c] = 3
        if out[r][new_max_c] != 6: out[r][new_max_c] = 3
    for c in c_divs:
        for r in range(new_min_r + 1, new_max_r):
            if out[r][c] != 6: out[r][c] = 3
    return out