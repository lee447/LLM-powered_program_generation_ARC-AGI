import math

def solve(grid):
    h, w = len(grid), len(grid[0])
    colors = sorted({c for row in grid for c in row if c != 0})
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
    for c in colors:
        minr, maxr, minc, maxc = bboxes[c]
        bh = maxr - minr + 1
        bw = maxc - minc + 1
        m = [[0]*3 for _ in range(3)]
        for i in range(3):
            r0 = minr + (i*bh)//3
            r1 = minr + ((i+1)*bh)//3 - 1
            if i == 2: r1 = maxr
            for j in range(3):
                c0 = minc + (j*bw)//3
                c1 = minc + ((j+1)*bw)//3 - 1
                if j == 2: c1 = maxc
                found = False
                for rr in range(r0, r1+1):
                    for cc in range(c0, c1+1):
                        if grid[rr][cc] == c:
                            found = True
                            break
                    if found: break
                if found:
                    m[i][j] = c
        masks[c] = m
    order = sorted(colors, key=lambda c: (bboxes[c][1]-bboxes[c][0]+1)*(bboxes[c][3]-bboxes[c][2]+1), reverse=True)
    out = [[0]*3 for _ in range(3)]
    for c in order:
        m = masks[c]
        for i in range(3):
            for j in range(3):
                if m[i][j] == c:
                    out[i][j] = c
    return out