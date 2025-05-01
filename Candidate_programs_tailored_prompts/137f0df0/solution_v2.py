def solve(grid):
    h = len(grid)
    w = len(grid[0])
    row_ints = []
    col_ints = []
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==5 and grid[r][c+1]==5 and grid[r+1][c]==5 and grid[r+1][c+1]==5:
                row_ints.append((r, r+1))
                col_ints.append((c, c+1))
    row_ints = sorted(set(row_ints))
    col_ints = sorted(set(col_ints))
    rs = []
    if row_ints:
        first_start = row_ints[0][0]
        if 0 <= first_start-1:
            rs.append((0, first_start-1, 'boundary'))
        for (p0,p1),(n0,n1) in zip(row_ints, row_ints[1:]):
            a = p1+1; b = n0-1
            if a<=b:
                rs.append((a,b,'interior'))
        last_end = row_ints[-1][1]
        if last_end+1<=h-1:
            rs.append((last_end+1,h-1,'boundary'))
    cs = []
    if col_ints:
        first_start = col_ints[0][0]
        if 0 <= first_start-1:
            cs.append((0, first_start-1, 'boundary'))
        for (p0,p1),(n0,n1) in zip(col_ints, col_ints[1:]):
            a = p1+1; b = n0-1
            if a<=b:
                cs.append((a,b,'interior'))
        last_end = col_ints[-1][1]
        if last_end+1<=w-1:
            cs.append((last_end+1,w-1,'boundary'))
    s_rows = set()
    for a,b,t in rs:
        for r in range(a,b+1):
            s_rows.add(r)
    out = [[0]*w for _ in range(h)]
    for a,b,t in rs:
        for r in range(a,b+1):
            if t=='interior':
                for c in range(w):
                    out[r][c] = 2
            else:
                for c in range(w):
                    out[r][c] = 1
    for a,b,t in cs:
        for c in range(a,b+1):
            if t=='interior':
                for r in range(h):
                    out[r][c] = 2
            else:
                for r in s_rows:
                    out[r][c] = 1
    for r in range(h):
        for c in range(w):
            if grid[r][c]==5:
                out[r][c]=5
    return out