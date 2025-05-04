def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    vth = rows//2+1
    bar_cols = []
    for j in range(cols):
        cnt = {}
        for i in range(rows):
            v = grid[i][j]
            if v:
                cnt[v] = cnt.get(v,0)+1
        mc = max(cnt.values()) if cnt else 0
        c = max(cnt, key=cnt.get) if cnt else 0
        if c and mc>=vth:
            bar_cols.append(j)
    bar_cols.sort()
    non_bar_cols = cols - len(bar_cols)
    rth = non_bar_cols//2+1
    bar_rows = []
    for i in range(rows):
        cnt = {}
        for j in range(cols):
            if j not in bar_cols:
                v = grid[i][j]
                if v:
                    cnt[v] = cnt.get(v,0)+1
        if cnt:
            mc = max(cnt.values())
            c = max(cnt, key=cnt.get)
            if c and mc>=rth:
                bar_rows.append(i)
    bar_rows.sort()
    new_cols = []
    if bar_cols and bar_cols[0]>0:
        new_cols.append(bar_cols[0]-1)
    for idx,b in enumerate(bar_cols):
        new_cols.append(b)
        if idx<len(bar_cols)-1:
            new_cols.append(b+1)
        elif b<cols-1:
            new_cols.append(b+1)
    new_rows = []
    if bar_rows and bar_rows[0]>0:
        new_rows.append(bar_rows[0]-1)
    for idx,r in enumerate(bar_rows):
        new_rows.append(r)
        if idx<len(bar_rows)-1:
            new_rows.append(r+1)
        elif r<rows-1:
            new_rows.append(r+1)
    return [[grid[r][c] for c in new_cols] for r in new_rows]