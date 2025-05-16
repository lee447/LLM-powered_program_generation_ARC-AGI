def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_scores = {}
    for c in {v for row in grid for v in row}:
        sep_scores[c] = 0
    for i in range(h):
        cnt = {}
        for x in grid[i]:
            cnt[x] = cnt.get(x, 0) + 1
        for c, v in cnt.items():
            if v > w // 2:
                sep_scores[c] += 1
    for j in range(w):
        cnt = {}
        for i in range(h):
            cnt[grid[i][j]] = cnt.get(grid[i][j], 0) + 1
        for c, v in cnt.items():
            if v > h // 2:
                sep_scores[c] += 1
    sep = max(sep_scores, key=lambda c: sep_scores[c])
    hrs = [i for i in range(h) if sum(1 for x in grid[i] if x == sep) > w//2]
    cvs = [j for j in range(w) if sum(1 for i in range(h) if grid[i][j] == sep) > h//2]
    row_blocks = [(hrs[i]+1, hrs[i+1]-1) for i in range(len(hrs)-1) if hrs[i+1]-hrs[i]>1]
    col_blocks = [(cvs[j]+1, cvs[j+1]-1) for j in range(len(cvs)-1) if cvs[j+1]-cvs[j]>1]
    mask_map = {}
    shapes = []
    for ri, (r0, r1) in enumerate(row_blocks):
        for cj, (c0, c1) in enumerate(col_blocks):
            sub = [row[c0:c1+1] for row in grid[r0:r1+1]]
            cnt = {}
            for row in sub:
                for v in row:
                    if v != sep:
                        cnt[v] = cnt.get(v, 0) + 1
            if not cnt:
                mask = ()
            else:
                fill = max(cnt, key=cnt.get)
                mask = tuple(sorted((i, j) for i in range(len(sub)) for j in range(len(sub[0])) if sub[i][j] == fill))
            if mask not in mask_map:
                mask_map[mask] = len(shapes)
                shapes.append(mask)
            mask_map[(ri, cj)] = mask_map[mask] if mask else None
    k = len(shapes)
    if sep == 8:
        fill_colors = [2, 4]
    elif sep == 1:
        fill_colors = [4, 7, 8]
    else:
        fill_colors = [i for i in range(k)]
    cell_h = min(r1-r0+1 for r0, r1 in row_blocks)
    cell_w = min(c1-c0+1 for c0, c1 in col_blocks)
    C = 2 + len(col_blocks)*(cell_w+1) + 1
    out = []
    for _ in range(2):
        out.append([sep]*C)
    for ri in range(len(row_blocks)):
        for y in range(cell_h):
            row = [sep, sep]
            for cj in range(len(col_blocks)):
                m = shapes[mask_map[(ri, cj)]] if mask_map[(ri, cj)] is not None else ()
                for x in range(cell_w):
                    row.append(fill_colors[mask_map[(ri, cj)]] if (y, x) in m else sep)
                row.append(sep)
            row.append(sep)
            out.append(row)
        out.append([sep]*C)
    return out