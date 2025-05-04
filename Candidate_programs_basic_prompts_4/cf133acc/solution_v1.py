def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for color in range(1, 10):
        for r in range(h):
            segs = []
            c = 0
            while c < w:
                if grid[r][c] == color:
                    start = c
                    while c < w and grid[r][c] == color:
                        c += 1
                    segs.append((start, c - 1))
                else:
                    c += 1
            if len(segs) == 2 and segs[1][0] - segs[0][1] == 2:
                gap = segs[0][1] + 1
                out[r][gap] = color
                for dr in (-1, 1):
                    rr = r + dr
                    while 0 <= rr < h and grid[rr][gap] == 0:
                        out[rr][gap] = color
                        rr += dr
        for c in range(w):
            segs = []
            r = 0
            while r < h:
                if grid[r][c] == color:
                    start = r
                    while r < h and grid[r][c] == color:
                        r += 1
                    segs.append((start, r - 1))
                else:
                    r += 1
            if len(segs) == 2 and segs[1][0] - segs[0][1] == 2:
                gap = segs[0][1] + 1
                out[gap][c] = color
                for dc in (-1, 1):
                    cc = c + dc
                    while 0 <= cc < w and grid[gap][cc] == 0:
                        out[gap][cc] = color
                        cc += dc
    return out