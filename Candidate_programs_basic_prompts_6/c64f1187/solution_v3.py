def solve(grid):
    H = len(grid)
    W = len(grid[0])
    ones = [(r,c) for r in range(H) for c in range(W) if grid[r][c]==1]
    one_set = set(ones)
    visited = set()
    shapes = {}
    for r,c in ones:
        if (r,c) in visited: continue
        stack = [(r,c)]
        visited.add((r,c))
        cluster = [(r,c)]
        while stack:
            rr,cc = stack.pop()
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc = rr+dr, cc+dc
                if (nr,nc) in one_set and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    stack.append((nr,nc))
                    cluster.append((nr,nc))
        minr = min(rr for rr,cc in cluster)
        maxr = max(rr for rr,cc in cluster)
        minc = min(cc for rr,cc in cluster)
        maxc = max(cc for rr,cc in cluster)
        h = maxr-minr+1
        w = maxc-minc+1
        pr = minr-1
        pc = minc-1
        color = grid[pr][pc]
        mask = [[0]*w for _ in range(h)]
        for rr,cc in cluster:
            mask[rr-minr][cc-minc] = 1
        shapes[color] = mask
    grey = [(r,c) for r in range(H) for c in range(W) if grid[r][c]==5]
    if not grey:
        return []
    rmin = min(r for r,c in grey)
    rmax = max(r for r,c in grey)
    cmin = min(c for r,c in grey)
    cmax = max(c for r,c in grey)
    out_h = rmax-rmin+1
    out_w = cmax-cmin+1
    out = [[0]*out_w for _ in range(out_h)]
    rows = sorted({r-rmin for r,c in grey})
    row_runs = []
    i = 0
    while i < len(rows):
        start = rows[i]
        length = 1
        i += 1
        while i < len(rows) and rows[i] == start+length:
            length += 1
            i += 1
        row_runs.append((start,length))
    cols = sorted({c-cmin for r,c in grey})
    col_runs = []
    i = 0
    while i < len(cols):
        start = cols[i]
        length = 1
        i += 1
        while i < len(cols) and cols[i] == start+length:
            length += 1
            i += 1
        col_runs.append((start,length))
    for roff,height in row_runs:
        for coff,width in col_runs:
            gr = rmin + roff
            gc = cmin + coff
            color = None
            for dr in range(height):
                if color is not None: break
                for dc in range(width):
                    v = grid[gr+dr][gc+dc]
                    if v!=5 and v!=0:
                        color = v
                        break
            if color is None: continue
            mask = shapes.get(color)
            if mask is None: continue
            h2 = len(mask)
            w2 = len(mask[0])
            for i in range(h2):
                for j in range(w2):
                    if mask[i][j]:
                        out[roff+i][coff+j] = color
    return out