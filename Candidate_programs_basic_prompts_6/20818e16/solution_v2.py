def solve(grid):
    bg = grid[0][0]
    boxes = {}
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v != bg:
                if v not in boxes:
                    boxes[v] = [i, i, j, j]
                else:
                    b = boxes[v]
                    b[0] = min(b[0], i)
                    b[1] = max(b[1], i)
                    b[2] = min(b[2], j)
                    b[3] = max(b[3], j)
    areas = {c: (boxes[c][1] - boxes[c][0] + 1) * (boxes[c][3] - boxes[c][2] + 1) for c in boxes}
    bgc = max(areas, key=lambda c: areas[c])
    h = boxes[bgc][1] - boxes[bgc][0] + 1
    w = boxes[bgc][3] - boxes[bgc][2] + 1
    out = [[bgc] * w for _ in range(h)]
    others = sorted((c for c in boxes if c != bgc), key=lambda c: areas[c], reverse=True)
    for c in others:
        bh, bw = boxes[c][1] - boxes[c][0] + 1, boxes[c][3] - boxes[c][2] + 1
        for i in range(bh):
            for j in range(bw):
                out[i][j] = c
    return out