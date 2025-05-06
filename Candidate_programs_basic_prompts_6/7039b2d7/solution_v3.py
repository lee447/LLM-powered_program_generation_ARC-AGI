def solve(grid):
    h = len(grid)
    w = len(grid[0])
    H = [i for i in range(h) if len(set(grid[i]))==1]
    V = [j for j in range(w) if len({grid[i][j] for i in range(h)})==1]
    rs = []
    prev = 0
    for i in H:
        if prev<=i-1: rs.append((prev,i-1))
        prev = i+1
    if prev<=h-1: rs.append((prev,h-1))
    cs = []
    prev = 0
    for j in V:
        if prev<=j-1: cs.append((prev,j-1))
        prev = j+1
    if prev<=w-1: cs.append((prev,w-1))
    out = []
    for r0,r1 in rs:
        row = []
        for c0,c1 in cs:
            cnt = {}
            for i in range(r0,r1+1):
                for j in range(c0,c1+1):
                    cnt[grid[i][j]] = cnt.get(grid[i][j],0)+1
            row.append(max(cnt,key=cnt.get))
        out.append(row)
    return out