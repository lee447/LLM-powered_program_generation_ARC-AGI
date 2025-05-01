def solve(grid):
    R, C = len(grid), len(grid[0])
    out = [[0]*C for _ in range(R)]
    zone_w = 3
    diag = {(0,2),(1,1),(2,0)}
    border = {(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2)}
    topbar = {(0,0),(0,1),(0,2)}
    botbar = {(2,0),(2,1),(2,2)}
    for zi in range(C//zone_w):
        c0 = zi*zone_w
        coords = set()
        for r in range(R):
            for c in range(c0,c0+zone_w):
                if grid[r][c] == 5:
                    coords.add((r, c-c0))
        if coords == border:
            color = 3
        elif coords == diag:
            color = 9
        elif coords == topbar:
            color = 6
        elif coords == botbar:
            color = 1
        elif len(coords) == 1:
            color = 4
        else:
            color = 0
        for r in range(R):
            for c in range(c0,c0+zone_w):
                out[r][c] = color
    return out