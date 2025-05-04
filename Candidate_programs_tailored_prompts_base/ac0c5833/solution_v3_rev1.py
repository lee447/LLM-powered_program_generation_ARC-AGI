from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    anchors = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 4]
    reds = {(i, j) for i in range(h) for j in range(w) if grid[i][j] == 2}
    visited = set()
    clusters = []
    for r, c in reds:
        if (r, c) in visited:
            continue
        stack = [(r, c)]
        comp = set()
        while stack:
            x, y = stack.pop()
            if (x, y) in comp:
                continue
            comp.add((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) in reds and (nx, ny) not in comp:
                    stack.append((nx, ny))
        visited |= comp
        clusters.append(comp)
    if not clusters:
        return grid
    # assume one cluster defines the pattern
    comp = clusters[0]
    # find the anchor closest to that cluster
    cr = sum(x for x, y in comp) / len(comp)
    cc = sum(y for x, y in comp) / len(comp)
    base = min(anchors, key=lambda p: abs(p[0] - cr) + abs(p[1] - cc))
    offsets = [(x - base[0], y - base[1]) for x, y in comp]
    out = [row[:] for row in grid]
    for ax, ay in anchors:
        if (ax, ay) == base:
            orient = offsets
        else:
            orient = [(-dx, -dy) for dx, dy in offsets]
        ok = True
        for dx, dy in orient:
            x, y = ax + dx, ay + dy
            if not (0 <= x < h and 0 <= y < w and out[x][y] == 0):
                ok = False
                break
        if not ok:
            continue
        for dx, dy in orient:
            x, y = ax + dx, ay + dy
            out[x][y] = 2
    return out