def solve(grid):
    nrows, ncols = len(grid), len(grid[0])
    mask = [[False]*ncols for _ in range(nrows)]
    clusters = []
    def is_checker(i,j,s):
        vals = set(grid[i+p][j+q] for p in range(s) for q in range(s))
        if 0 in vals or len(vals)!=2: return False
        v1,v2 = list(vals)
        def check(a,b):
            for p in range(s):
                for q in range(s):
                    exp = a if ((p+q)&1)==0 else b
                    if grid[i+p][j+q]!=exp: return False
            return True
        return check(v1,v2) or check(v2,v1)
    for s in (3,2):
        for i in range(nrows-s+1):
            for j in range(ncols-s+1):
                if any(mask[i+p][j+q] for p in range(s) for q in range(s)): continue
                if is_checker(i,j,s):
                    sub = [row[j:j+s] for row in grid[i:i+s]]
                    clusters.append((i,i+s-1,j,j+s-1,sub))
                    for p in range(s):
                        for q in range(s):
                            mask[i+p][j+q] = True
    clusters.sort(key=lambda x:(-x[3], x[0]))
    placed = []
    for r0,r1,c0,c1,sub in clusters:
        s = c1-c0+1
        for new_c1 in range(ncols-1, s-2, -1):
            new_c0 = new_c1 - (s-1)
            ok = True
            for pr0,pr1,pc0,pc1,_ in placed:
                if not (r1 < pr0 or r0 > pr1):
                    if not (new_c1 < pc0 or new_c0 > pc1):
                        ok = False; break
            if ok:
                placed.append((r0, r1, new_c0, new_c1, sub))
                break
    out = [[0]*ncols for _ in range(nrows)]
    for r0,r1,c0,c1,sub in placed:
        for p in range(r1-r0+1):
            for q in range(c1-c0+1):
                out[r0+p][c0+q] = sub[p][q]
    return out