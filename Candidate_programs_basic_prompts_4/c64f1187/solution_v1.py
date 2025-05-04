def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    # find top shape anchor row
    anchor_row = None
    for r in range(rows):
        if any(grid[r][c] not in (0,1,5) for c in range(cols)) and r+1 < rows and any(grid[r+1][c] == 1 for c in range(cols)):
            anchor_row = r
            break
    # measure shape height
    h = 0
    for r in range(anchor_row+1, rows):
        if any(grid[r][c] == 1 for c in range(cols)):
            h += 1
        else:
            break
    # record shapes
    shapes = {}
    for c0 in range(cols):
        color = grid[anchor_row][c0]
        if color != 0:
            # find leftmost 1 in next row to locate block
            sc = None
            for c in range(c0+1, cols):
                if grid[anchor_row+1][c] == 1:
                    sc = c
                    break
            if sc is None:
                continue
            # measure shape width
            w = 0
            for c in range(sc, cols):
                if grid[anchor_row+1][c] == 1:
                    w += 1
                else:
                    break
            mat = [[0]*w for _ in range(h)]
            for dr in range(h):
                for dc in range(w):
                    if grid[anchor_row+1+dr][sc+dc] == 1:
                        mat[dr][dc] = 1
            shapes[color] = mat
    # find bottom region rows
    bottom = [r for r in range(rows) if any(grid[r][c] == 5 for c in range(cols))]
    if not bottom:
        return [[]]
    bottom.sort()
    rmin, rmax = bottom[0], bottom[-1]
    # group rows into pairs
    br = []
    i = 0
    while i < len(bottom):
        r0 = bottom[i]
        if i+1 < len(bottom) and bottom[i+1] == r0+1:
            br.append((r0, r0+1))
            i += 2
        else:
            i += 1
    groups = br
    # find micro-block columns (where 5 appears)
    five_cols = sorted({c for r in range(rmin, rmax+1) for c in range(cols) if grid[r][c] == 5})
    blocks = []
    j = 0
    while j < len(five_cols):
        c0 = five_cols[j]
        if j+1 < len(five_cols) and five_cols[j+1] == c0+1:
            blocks.append((c0, c0+1))
            j += 2
        else:
            j += 1
    # output dimensions
    G = len(groups)
    B = len(blocks)
    out_rows = G*2 + (G-1)
    out_cols = B*2 + (B-1)
    out = [[0]*out_cols for _ in range(out_rows)]
    # fill
    for gi, (r0, r1) in enumerate(groups):
        for bi, (c0, c1) in enumerate(blocks):
            for dr in (0,1):
                for dc in (0,1):
                    rr = r0 + dr
                    cc = c0 + dc
                    v = grid[rr][cc]
                    if v not in (0,5):
                        color = v
                        mat = shapes.get(color)
                        if not mat:
                            continue
                        orow = gi*3
                        ocol = bi*3
                        for dr2 in range(len(mat)):
                            for dc2 in range(len(mat[0])):
                                if mat[dr2][dc2]:
                                    out[orow+dr2][ocol+dc2] = color
    return out