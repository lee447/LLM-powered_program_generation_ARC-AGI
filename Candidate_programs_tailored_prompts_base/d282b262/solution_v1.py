def solve(grid):
    h = len(grid)
    w = len(grid[0])
    occupied = [[False]*w for _ in range(h)]
    clusters = []
    for size in (3,2):
        for i in range(h-size+1):
            for j in range(w-size+1):
                conflict = False
                for di in range(size):
                    for dj in range(size):
                        if occupied[i+di][j+dj] or grid[i+di][j+dj]==0:
                            conflict = True
                            break
                    if conflict: break
                if conflict: continue
                vals = {grid[i+di][j+dj] for di in range(size) for dj in range(size)}
                if len(vals)!=2: continue
                top = grid[i][j]
                other = next(v for v in vals if v!=top)
                p = (i+j)&1
                ok = True
                for di in range(size):
                    for dj in range(size):
                        expected = top if ((i+di+j+dj)&1)==p else other
                        if grid[i+di][j+dj]!=expected:
                            ok = False
                            break
                    if not ok: break
                if not ok: continue
                sub = [grid[i+di][j:j+size] for di in range(size)]
                idx = len(clusters)
                clusters.append({'i':i,'j':j,'size':size,'sub':sub})
                for di in range(size):
                    for dj in range(size):
                        occupied[i+di][j+dj] = True
    n = len(clusters)
    row_clusters = {}
    for idx,c in enumerate(clusters):
        for r in range(c['i'],c['i']+c['size']):
            row_clusters.setdefault(r,[]).append(idx)
    rows = sorted(row_clusters.keys(), key=lambda r: -len(row_clusters[r]))
    j_out = [None]*n
    for r in rows:
        grp = sorted(row_clusters[r], key=lambda c: clusters[c]['j'])
        if len(grp)>1:
            col_end = w-1
            for c in reversed(grp):
                sz = clusters[c]['size']
                if j_out[c] is None:
                    j_out[c] = col_end - (sz-1)
                col_end = min(col_end, j_out[c]-1)
        else:
            c = grp[0]
            if j_out[c] is None:
                j_out[c] = w - clusters[c]['size']
    out = [[0]*w for _ in range(h)]
    for c,info in enumerate(clusters):
        i,j0,sz = info['i'], j_out[c], info['size']
        sub = info['sub']
        for di in range(sz):
            for dj in range(sz):
                out[i+di][j0+dj] = sub[di][dj]
    return out