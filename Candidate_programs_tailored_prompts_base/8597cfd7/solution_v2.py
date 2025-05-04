def solve(grid):
    h = len(grid)
    w = len(grid[0])
    split = next(i for i, row in enumerate(grid) if all(cell == 5 for cell in row))
    anchors = []
    for c in range(w):
        for r in range(split):
            if grid[r][c] not in (0, 5):
                anchors.append(c)
                break
    anchors = anchors[:2]
    best_color = None
    best_count = -1
    for c in anchors:
        total = 0
        color = None
        for r in range(h):
            if r == split: continue
            v = grid[r][c]
            if v not in (0, 5):
                total += 1
                color = v
        if total > best_count:
            best_count = total
            best_color = color
    return [[best_color, best_color], [best_color, best_color]]