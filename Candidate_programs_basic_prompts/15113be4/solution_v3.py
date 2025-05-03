def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_rows = [r for r in range(h) if all(x==4 for x in grid[r])]
    sep_cols = [c for c in range(w) if all(grid[r][c]==4 for r in range(h))]
    row_bounds = []
    prev = -1
    for r in sep_rows+[h]:
        if r-prev-1>0:
            row_bounds.append((prev+1,r))
        prev = r
    col_bounds = []
    prev = -1
    for c in sep_cols+[w]:
        if c-prev-1>0:
            col_bounds.append((prev+1,c))
        prev = c
    br0,er0 = row_bounds[0]
    bc0,ec0 = col_bounds[0]
    pattern = []
    for r in range(br0,er0):
        row = []
        for c in range(bc0,ec0):
            row.append(1 if grid[r][c]!=0 else 0)
        pattern.append(row)
    ph, pw = len(pattern), len(pattern[0])
    out = [row[:] for row in grid]
    for bi,(br,er) in enumerate(row_bounds):
        for bj,(bc,ec) in enumerate(col_bounds):
            if bi==0 and bj==0: continue
            bh, bw = er-br, ec-bc
            if bh!=ph or bw!=pw:
                # small cell
                bh, bw = er-br, ec-bc
                # detect fill color
                cnt={}
                for r in range(br,er):
                    for c in range(bc,ec):
                        v = grid[r][c]
                        if v not in (0,1,4): cnt[v]=cnt.get(v,0)+1
                col = max(cnt,key=cnt.get) if cnt else 0
                for r in range(bh):
                    for c in range(bw):
                        if pattern[r*bh//ph][c*bw//pw] and out[br+r][bc+c]==0:
                            out[br+r][bc+c]=col
    return out