def solve(grid):
    R = len(grid)
    C = len(grid[0])
    sep_r = [i for i in range(R) if all(grid[i][j]==0 for j in range(C))]
    sep_c = [j for j in range(C) if all(grid[i][j]==0 for i in range(R))]
    br = len(sep_r)-1
    bc = len(sep_c)-1
    tr = sep_r[1]-sep_r[0]-1
    tc = sep_c[1]-sep_c[0]-1
    colors = {}
    for i in range(R):
        for j in range(C):
            v = grid[i][j]
            if v:
                colors[v] = colors.get(v,0)+1
    shape = min(colors, key=colors.get)
    back = max(colors, key=colors.get)
    out = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if grid[i][j]==0: continue
            bi = max(k for k in range(len(sep_r)) if sep_r[k]<i)
            bj = max(k for k in range(len(sep_c)) if sep_c[k]<j)
            li = i - sep_r[bi] - 1
            lj = j - sep_c[bj] - 1
            top = bi < br//2+1
            left = bj < bc//2+1
            vr = li < 2 if top else li >= tr-2
            hr = lj < 2 if left else lj >= tc-2
            out[i][j] = shape if vr and hr else back
    return out