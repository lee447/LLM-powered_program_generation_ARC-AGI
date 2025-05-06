def solve(grid):
    headerRow = next(r for r,row in enumerate(grid) if any(v not in (0,1,5) for v in row))
    shapeDefRows = [headerRow+1, headerRow+2]
    onesCols = sorted({c for r in shapeDefRows for c,v in enumerate(grid[r]) if v==1})
    clusters = []
    cur = []
    for c in onesCols:
        if not cur or c==cur[-1]+1:
            cur.append(c)
        else:
            clusters.append(cur)
            cur = [c]
    if cur: clusters.append(cur)
    shapes = {}
    for cl in clusters:
        w = len(cl)
        c0 = cl[0]
        color = grid[headerRow][c0-1]
        mask = [[1 if grid[shapeDefRows[i]][c0+j]==1 else 0 for j in range(w)] for i in range(2)]
        shapes[color] = mask
    rows5 = sorted({r for r,row in enumerate(grid) for v in row if v==5})
    rowBlocks = []
    cur = []
    for r in rows5:
        if not cur or r==cur[-1]+1:
            cur.append(r)
        else:
            rowBlocks.append(cur)
            cur = [r]
    if cur: rowBlocks.append(cur)
    cols5 = sorted({c for row in grid for c,v in enumerate(row) if v==5})
    colBlocks = []
    cur = []
    for c in cols5:
        if not cur or c==cur[-1]+1:
            cur.append(c)
        else:
            colBlocks.append(cur)
            cur = [c]
    if cur: colBlocks.append(cur)
    bh = len(next(iter(shapes.values())))
    bw = len(next(iter(shapes.values()))[0])
    R = len(rowBlocks)*(bh) + (len(rowBlocks)-1)
    C = len(colBlocks)*(bw) + (len(colBlocks)-1)
    out = [[0]*C for _ in range(R)]
    for i,rb in enumerate(rowBlocks):
        for j,cb in enumerate(colBlocks):
            label = None
            for r in rb:
                for c in cb:
                    if grid[r][c]!=5:
                        label = grid[r][c]
                        break
                if label is not None: break
            if label in shapes:
                mask = shapes[label]
                sr = i*(bh+1)
                sc = j*(bw+1)
                for di in range(len(mask)):
                    for dj in range(len(mask[0])):
                        if mask[di][dj]:
                            out[sr+di][sc+dj] = label
    return out