from typing import List, Tuple

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def neighbors(r,c):
        for dr,dc in dirs:
            nr,nc = r+dr, c+dc
            if 0 <= nr < h and 0 <= nc < w:
                yield nr,nc

    # find clusters of value v
    def find_clusters(v: int) -> List[List[Tuple[int,int]]]:
        vis = [[False]*w for _ in range(h)]
        clusters = []
        for i in range(h):
            for j in range(w):
                if not vis[i][j] and grid[i][j] == v:
                    q = [(i,j)]
                    vis[i][j] = True
                    comp = [(i,j)]
                    qi = 0
                    while qi < len(q):
                        r,c = q[qi]; qi += 1
                        for nr,nc in neighbors(r,c):
                            if not vis[nr][nc] and grid[nr][nc] == v:
                                vis[nr][nc] = True
                                q.append((nr,nc))
                                comp.append((nr,nc))
                    clusters.append(comp)
        return clusters

    # find template cluster of 2 in top-left
    twocl = find_clusters(2)
    # pick cluster with smallest (min_row, min_col)
    def cluster_minpos(cl):
        return min(cl)
    twocl.sort(key=lambda cl: cluster_minpos(cl))
    tpl = twocl[0]
    rs = [r for r,c in tpl]; cs = [c for r,c in tpl]
    r0t, r1t = min(rs), max(rs)
    c0t, c1t = min(cs), max(cs)
    Ht, Wt = r1t-r0t+1, c1t-c0t+1
    tpl_mask = [[0]*Wt for _ in range(Ht)]
    for r,c in tpl:
        tpl_mask[r-r0t][c-c0t] = 1

    out = [row[:] for row in grid]
    onecls = find_clusters(1)
    for cl in onecls:
        rs = [r for r,c in cl]; cs = [c for r,c in cl]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        H1, W1 = r1-r0+1, c1-c0+1
        if H1 % Ht or W1 % Wt: continue
        sy, sx = H1//Ht, W1//Wt
        expected = set()
        for i in range(Ht):
            for j in range(Wt):
                if tpl_mask[i][j]:
                    for di in range(sy):
                        for dj in range(sx):
                            expected.add((r0 + i*sy + di, c0 + j*sx + dj))
        if expected == set(cl):
            for r,c in cl:
                out[r][c] = 2

    return out