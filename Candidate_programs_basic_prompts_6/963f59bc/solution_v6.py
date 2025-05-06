def solve(grid):
    H, W = len(grid), len(grid[0])
    from collections import Counter
    cnt = Counter(grid[i][j] for i in range(H) for j in range(W) if grid[i][j] != 0)
    template_color = max((c for c in cnt if cnt[c] > 1), key=lambda c: cnt[c])
    template = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == template_color]
    seeds = [(i, j, grid[i][j]) for i in range(H) for j in range(W) if grid[i][j] != 0 and grid[i][j] != template_color]
    def rotate(v, r):
        i, j = v
        if r == 0: return ( i,  j)
        if r == 1: return (-j,  i)
        if r == 2: return (-i, -j)
        return ( j, -i)
    placements = []
    for si, sj, sc in seeds:
        found = None
        for ai, aj in template:
            rel = [(pi - ai, pj - aj) for pi, pj in template]
            for r in range(4):
                ok = True
                for di, dj in rel:
                    ri, rj = rotate((di, dj), r)
                    ni, nj = si + ri, sj + rj
                    if not (0 <= ni < H and 0 <= nj < W): ok = False; break
                    if (ri, rj) == (0, 0):
                        if grid[ni][nj] != sc: ok = False; break
                    else:
                        if grid[ni][nj] != 0: ok = False; break
                if ok:
                    found = (ai, aj, r)
                    break
            if found: break
        placements.append((si, sj, sc, found[0], found[1], found[2]))
    out = [row[:] for row in grid]
    for si, sj, sc, ai, aj, r in placements:
        rel = [(pi - ai, pj - aj) for pi, pj in template]
        for di, dj in rel:
            ri, rj = rotate((di, dj), r)
            ni, nj = si + ri, sj + rj
            out[ni][nj] = sc
    return out