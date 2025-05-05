def solve(grid):
    h = len(grid)
    w = len(grid[0])
    bw = w // 3
    top = {(0,0),(0,1),(0,2)}
    mid = {(1,0),(1,1),(1,2)}
    bot = {(2,0),(2,1),(2,2)}
    center = {(1,1)}
    diag = {(0,2),(1,1),(2,0)}
    border = {(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2)}
    out = [[0]*w for _ in range(h)]
    for b in range(3):
        pts = set()
        for r in range(h):
            for c in range(b*bw,(b+1)*bw):
                if grid[r][c] == 5:
                    pts.add((r, c - b*bw))
        if pts == top:
            color = 6
        elif pts == bot:
            color = 1
        elif pts == border:
            color = 3
        elif pts == center:
            color = 4
        elif pts == diag:
            color = 9
        else:
            color = 0
        for r in range(h):
            for c in range(b*bw,(b+1)*bw):
                out[r][c] = color
    return out