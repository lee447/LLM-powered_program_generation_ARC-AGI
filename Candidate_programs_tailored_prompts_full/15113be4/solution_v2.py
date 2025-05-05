def solve(grid):
    h, w = len(grid), len(grid[0])
    grey = 4
    grey_rows = {i for i,row in enumerate(grid) if all(c==grey for c in row)}
    grey_cols = {j for j in range(w) if all(grid[i][j]==grey for i in range(h))}
    interior_rows = [i for i in range(h) if i not in grey_rows]
    interior_cols = [j for j in range(w) if j not in grey_cols]
    row_clusters, col_clusters = [], []
    curr = []
    for i in interior_rows:
        if not curr or i==curr[-1]+1:
            curr.append(i)
        else:
            row_clusters.append(curr)
            curr=[i]
    if curr: row_clusters.append(curr)
    curr = []
    for j in interior_cols:
        if not curr or j==curr[-1]+1:
            curr.append(j)
        else:
            col_clusters.append(curr)
            curr=[j]
    if curr: col_clusters.append(curr)
    br, bc = len(row_clusters), len(col_clusters)
    bh = len(row_clusters[0])
    bw = len(col_clusters[0])
    accent = {v for row in grid for v in row if v not in (0,1,grey)}
    ac = accent.pop() if accent else None
    out = [row[:] for row in grid]
    for bi in range(br):
        for bj in range(bc):
            idx = bi*bc + bj
            for r in range(bh):
                i = row_clusters[bi][r]
                lc = (r+idx) % bw
                j = col_clusters[bj][lc]
                out[i][j] = ac
    return out