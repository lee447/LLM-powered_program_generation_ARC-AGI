def solve(grid):
    n, m = len(grid), len(grid[0])
    from collections import Counter, deque
    # detect background as most common on border
    border = []
    for j in range(m):
        border.append(grid[0][j]); border.append(grid[n-1][j])
    for i in range(n):
        border.append(grid[i][0]); border.append(grid[i][m-1])
    bg = Counter(border).most_common(1)[0][0]
    # find uniform rows
    band_rows = [i for i in range(n) if len(set(grid[i]))==1 and grid[i][0]!=bg]
    segs = []
    for i in band_rows:
        if not segs or i != segs[-1][-1]+1:
            segs.append([i,i])
        else:
            segs[-1][1] = i
    band_r = max(segs, key=lambda x: x[1]-x[0])
    if band_r:
        orientation = 'h'; r0, r1 = band_r; thickness = r1-r0+1; span = m
    else:
        # find uniform cols
        band_cols = []
        for j in range(m):
            col = [grid[i][j] for i in range(n)]
            if len(set(col))==1 and col[0]!=bg: band_cols.append(j)
        segs = []
        for j in band_cols:
            if not segs or j != segs[-1][-1]+1:
                segs.append([j,j])
            else:
                segs[-1][1] = j
        c0, c1 = max(segs, key=lambda x: x[1]-x[0])
        orientation = 'v'; thickness = c1-c0+1; span = n
        r0 = c0; r1 = c1
    # choose corner
    if orientation=='h':
        top = (r0 + r1)//2 < n/2
        if top:
            sr = r1+1; sc = 0
        else:
            sr = r0-thickness; sc = 0
    else:
        left = (r0 + r1)//2 < m/2
        if left:
            sr = 0; sc = r1+1
        else:
            sr = 0; sc = r0-thickness
    # extract
    out = []
    for i in range(sr, sr+thickness):
        row = grid[i][sc:sc+span]
        out.append(row)
    return out