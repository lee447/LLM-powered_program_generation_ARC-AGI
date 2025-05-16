from collections import Counter

def solve(grid):
    h, w = len(grid), len(grid[0])
    border_color = grid[0][0]
    is_border_row = [all(x == border_color for x in row) for row in grid]
    is_border_col = [all(grid[i][j] == border_color for i in range(h)) for j in range(w)]
    rows = []
    i = 0
    while i < h:
        if not is_border_row[i]:
            j = i
            while j < h and not is_border_row[j]:
                j += 1
            rows.append((i, j))
            i = j
        else:
            i += 1
    cols = []
    j = 0
    while j < w:
        if not is_border_col[j]:
            k = j
            while k < w and not is_border_col[k]:
                k += 1
            cols.append((j, k))
            j = k
        else:
            j += 1
    if len(rows) == 1:
        r0, r1 = rows[0]
        m = (r0 + r1) // 2
        rows = [(r0, m), (m, r1)]
    if len(cols) == 1:
        c0, c1 = cols[0]
        m = (c0 + c1) // 2
        cols = [(c0, m), (m, c1)]
    RR, CC = len(rows), len(cols)
    background = [[0]*CC for _ in range(RR)]
    shapes = [[[] for _ in range(CC)] for _ in range(RR)]
    dims = [[None]*CC for _ in range(RR)]
    for ri, (r0, r1) in enumerate(rows):
        for cj, (c0, c1) in enumerate(cols):
            cnt = Counter(grid[x][y] for x in range(r0, r1) for y in range(c0, c1))
            bg = cnt.most_common(1)[0][0]
            background[ri][cj] = bg
            H, W = r1 - r0, c1 - c0
            dims[ri][cj] = (H, W)
            vals = [(col, cnt[col]) for col in cnt if col != bg and col != border_color]
            if vals:
                shape_color = max(vals, key=lambda x: x[1])[0]
            else:
                shape_color = None
            pts = []
            if shape_color is not None:
                for x in range(r0, r1):
                    for y in range(c0, c1):
                        if grid[x][y] == shape_color:
                            pts.append((x - r0, y - c0, shape_color))
            shapes[ri][cj] = pts
    mapping = {(0,0):(1,0),(1,0):(1,1),(1,1):(0,1),(0,1):(0,0)}
    out = [row[:] for row in grid]
    for ri, (r0, r1) in enumerate(rows):
        for cj, (c0, c1) in enumerate(cols):
            bg = background[ri][cj]
            for x in range(r0, r1):
                for y in range(c0, c1):
                    if out[x][y] != border_color:
                        out[x][y] = bg
    for (di, dj), (si, sj) in mapping.items():
        r0d, _ = rows[di]
        c0d, _ = cols[dj]
        for dr, dc, col in shapes[si][sj]:
            nr, nc = dc, dims[si][sj][0] - 1 - dr
            x = r0d + nr
            y = c0d + nc
            if 0 <= x < h and 0 <= y < w and out[x][y] != border_color:
                out[x][y] = col
    return out