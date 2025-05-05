def solve(grid):
    h, w = len(grid), len(grid[0])
    band = next(i for i in range(h) if all(grid[i][j] == 5 for j in range(w)))
    stripes = [j for j in range(w) if any(grid[i][j] not in (0,5) for i in range(h))]
    best_color, best_score = None, None
    for j in stripes:
        above = below = 0
        color = None
        for i in range(h):
            v = grid[i][j]
            if v not in (0,5):
                color = v
                if i < band: above += 1
                elif i > band: below += 1
        score = below - above
        if best_score is None or score > best_score:
            best_score, best_color = score, color
    return [[best_color, best_color], [best_color, best_color]]