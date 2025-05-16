def solve(grid):
    h, w = len(grid), len(grid[0])
    sep, bg = 5, max(set(sum(grid, [])), key=sum(grid, []).count)
    hrs = [i for i in range(h) if sum(1 for x in grid[i] if x == sep) > w//2]
    cvs = [j for j in range(w) if sum(1 for i in range(h) if grid[i][j] == sep) > h//2]
    row_blocks = [(hrs[i]+1, hrs[i+1]-1) for i in range(len(hrs)-1) if hrs[i+1]-hrs[i]>1]
    col_blocks = [(cvs[j]+1, cvs[j+1]-1) for j in range(len(cvs)-1) if cvs[j+1]-cvs[j]>1]
    shapes, order = [], {}
    for ri, (r0, r1) in enumerate(row_blocks):
        for cj, (c0, c1) in enumerate(col_blocks):
            sub = [row[c0:c1+1] for row in grid[r0:r1+1]]
            cnt = {}
            for row in sub:
                for v in row:
                    if v not in (sep, bg):
                        cnt[v] = cnt.get(v,0)+1
            fill = max(cnt, key=cnt.get) if cnt else None
            mask = tuple((i,j) for i in range(len(sub)) for j in range(len(sub[0])) if sub[i][j]==fill)
            if mask not in order:
                order[mask] = len(shapes)
                shapes.append(mask)
    k = len(shapes)
    fills = sorted([c for c in range(10) if c not in (sep,bg)])[-k:]
    R = 1 + len(row_blocks)*(max(r1-r0+1 for r0,r1 in row_blocks)+1) + 0
    C = 1 + len(col_blocks)*(max(c1-c0+1 for c0,c1 in col_blocks)+1) + 0
    out = [[sep]*C for _ in range(R)]
    for i in range(R):
        out[i][0] = sep
        out[i][-1] = sep
    for j in range(C):
        out[0][j] = sep
        out[-1][j] = sep
    cell_h = max(r1-r0+1 for r0,r1 in row_blocks)
    cell_w = max(c1-c0+1 for c0,c1 in col_blocks)
    for ri in range(len(row_blocks)):
        for cj in range(len(col_blocks)):
            r0 = 1 + ri*(cell_h+1)
            c0 = 1 + cj*(cell_w+1)
            orig = shapes[order[tuple((i,j) for i in range(len(sub)) for j in range(len(sub[0])) if sub[i][j]==fill)]]
            idx = order[tuple(orig)]
            for (i,j) in shapes[idx]:
                out[r0+i][c0+j] = fills[idx]
    return out