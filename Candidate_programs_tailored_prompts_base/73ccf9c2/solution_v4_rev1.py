from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    color = next((v for row in grid for v in row if v), 0)
    pts = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == color]
    visited = [[False]*m for _ in range(n)]
    comps = []
    for i, j in pts:
        if visited[i][j]: continue
        stack = [(i, j)]
        comp = []
        visited[i][j] = True
        while stack:
            x, y = stack.pop()
            comp.append((x, y))
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx or dy:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == color:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
        comps.append(comp)
    comps.sort(key=len)
    rels = []
    for comp in comps:
        rs = [p[0] for p in comp]; cs = [p[1] for p in comp]
        mnx, mxx = min(rs), max(rs); mny, mxy = min(cs), max(cs)
        cx2, cy2 = mnx+mxx, mny+mxy
        rels.append({(2*r-cx2, 2*c-cy2) for r,c in comp})
    common = rels[0]
    rots = [lambda d: d, lambda d: (-d[1], d[0]), lambda d: (-d[0], -d[1]), lambda d: (d[1], -d[0])]
    for rel in rels[1:]:
        best = set()
        for f in rots:
            rset = {f(d) for d in rel}
            inter = common & rset
            if len(inter) > len(best):
                best = inter; bestr = rset
        common = best
    drs = [d[0] for d in common]; dcs = [d[1] for d in common]
    minr, maxr = min(drs), max(drs); minc, maxc = min(dcs), max(dcs)
    H = (maxr-minr)//2+1; W = (maxc-minc)//2+1
    out = [[0]*W for _ in range(H)]
    for dr,dc in common:
        r = (dr-minr)//2; c = (dc-minc)//2
        out[r][c] = color
    return out