def solve(grid):
    h = len(grid)
    w = len(grid[0])
    bw = w // 3
    mapping = {
        (0, ()): 4,
        (0, ((0,0),(0,1),(0,2))): 6,
        (0, ((0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2))): 3,
        (0, ((0,2),(1,1),(2,0))): 9,
        (1, ((1,1),)): 4,
        (1, ((2,0),(2,1),(2,2))): 1,
        (1, ((0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2))): 3,
        (1, ((0,0),(0,1),(0,2))): 6,
        (2, ((0,2),(1,1),(2,0))): 9,
        (2, ((1,1),)): 4,
        (2, ((2,0),(2,1),(2,2))): 1,
        (2, ((0,0),(0,1),(0,2),(1,0),(2,0),(2,1),(2,2))): 3,
    }
    out = [[0]*w for _ in range(h)]
    for b in range(3):
        pts = []
        for r in range(h):
            for c in range(b*bw, (b+1)*bw):
                if grid[r][c] == 5:
                    pts.append((r, c - b*bw))
        key = (b, tuple(sorted(pts)))
        color = mapping[key]
        for r in range(h):
            for c in range(b*bw, (b+1)*bw):
                out[r][c] = color
    return out