def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import Counter
    cnt = Counter(c for row in grid for c in row)
    bg, _ = max(cnt.items(), key=lambda x: x[1])
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    centers = []
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != bg:
                ok = True
                for dr,dc in dirs:
                    nr,nc = r+dr, c+dc
                    if not (0<=nr<h and 0<=nc<w and grid[nr][nc]==v):
                        ok = False; break
                if ok:
                    centers.append((r,c,v))
    def get_seeds(r,c,pc):
        best = (0,None,[])
        for dr,dc in dirs:
            k = 1
            while 0<=r+dr*k<h and 0<=c+dc*k<w and grid[r+dr*k][c+dc*k]==pc:
                k += 1
            seeds = []
            j = k
            while 0<=r+dr*j<h and 0<=c+dc*j<w and grid[r+dr*j][c+dc*j]!=bg and grid[r+dr*j][c+dc*j]!=pc:
                seeds.append(grid[r+dr*j][c+dc*j])
                j += 1
            if len(seeds) > best[0]:
                best = (len(seeds),(dr,dc),seeds)
        return best
    rep = []
    for r,c,pc in centers:
        ln, d, s = get_seeds(r,c,pc)
        rep.append((ln,(r,c,pc),d,s))
    rep.sort(key=lambda x: x[0], reverse=True)
    big_ln,(br,bc,bp),big_dir,big_seeds = rep[0]
    small_ln,(sr,sc,sp),small_dir,small_seeds = rep[1]
    s_seeds = small_seeds
    b_seeds = big_seeds
    pattern = []
    if len(s_seeds) >= 2:
        pattern = s_seeds
    elif len(s_seeds) == 1 and len(b_seeds) >= 1:
        pattern = [s_seeds[0], b_seeds[0]]
    else:
        pattern = b_seeds[:2]
    dr,dc = big_dir
    fill_dr, fill_dc = -dc, dr
    for k in range(1, max(h,w)+1):
        r = sr + fill_dr*k
        c = sc + fill_dc*k
        if not (0<=r<h and 0<=c<w) or grid[r][c] != bg:
            break
        grid[r][c] = pattern[(k-1) % len(pattern)]
    return grid