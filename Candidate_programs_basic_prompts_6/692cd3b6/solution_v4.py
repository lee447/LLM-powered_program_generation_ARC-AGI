from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    (r1, c1), (r2, c2) = pts[0], pts[1]
    dx, dy = c2 - c1, r2 - r1
    path = set()
    th = 1
    if abs(dx) < abs(dy):
        # horizontal first
        step = 1 if dx > 0 else -1
        for dc in range(0, dx + step, step):
            cc = c1 + dc
            for dr in (-th, 0, th):
                path.add((r1 + dr, cc))
        step = 1 if dy > 0 else -1
        for dr in range(step, dy + step, step):
            rr = r1 + dr
            for dc in (-th, 0, th):
                path.add((rr, c2 + dc))
    else:
        # vertical first
        step = 1 if dy > 0 else -1
        for dr in range(0, dy + step, step):
            rr = r1 + dr
            for dc in (-th, 0, th):
                path.add((rr, c1 + dc))
        step = 1 if dx > 0 else -1
        for dc in range(step, dx + step, step):
            cc = c1 + dc
            for dr in (-th, 0, th):
                path.add((r2 + dr, cc))
    out = [row[:] for row in grid]
    for r, c in path:
        if 0 <= r < h and 0 <= c < w and out[r][c] == 0:
            out[r][c] = 4
    return out