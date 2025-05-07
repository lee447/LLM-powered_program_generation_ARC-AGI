def solve(grid):
    from math import floor
    h, w = len(grid), len(grid[0])
    colors = set(c for row in grid for c in row if c != 0)
    bboxes = {}
    for c in colors:
        minr, maxr, minc, maxc = h, -1, w, -1
        for i in range(h):
            for j in range(w):
                if grid[i][j] == c:
                    minr = min(minr, i); maxr = max(maxr, i)
                    minc = min(minc, j); maxc = max(maxc, j)
        bboxes[c] = (minr, maxr, minc, maxc)
    masks = {}
    for c, (minr, maxr, minc, maxc) in bboxes.items():
        bh = maxr - minr
        bw = maxc - minc
        m = [[0]*3 for _ in range(3)]
        for y in range(3):
            for x in range(3):
                sy = minr + int(round(y * bh / 2))
                sx = minc + int(round(x * bw / 2))
                if 0 <= sy < h and 0 <= sx < w and grid[sy][sx] == c:
                    m[y][x] = c
        masks[c] = m
    # draw larger shapes first
    order = sorted(colors, key=lambda c: (bboxes[c][1]-bboxes[c][0]+1)*(bboxes[c][3]-bboxes[c][2]+1), reverse=True)
    out = [[0]*3 for _ in range(3)]
    for c in order:
        m = masks[c]
        for i in range(3):
            for j in range(3):
                if m[i][j] == c:
                    out[i][j] = c
    return out