def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    band_width = cols // 3
    clusters = {0: [], 1: [], 2: []}
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 5:
                b = c // band_width
                clusters[b].append((r, c % band_width))
    shape2color = {
        ((0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2)): 3,
        ((1,1),): 4,
        ((0,2),(1,1),(2,0)): 9,
        ((2,0),(2,1),(2,2)): 1,
        ((0,0),(0,1),(0,2)): 6
    }
    out = [[0]*cols for _ in range(rows)]
    for b, coords in clusters.items():
        key = tuple(sorted(coords))
        color = shape2color[key]
        start = b * band_width
        for r in range(rows):
            for c in range(start, start + band_width):
                out[r][c] = color
    return out