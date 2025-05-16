from collections import deque, Counter

def solve(grid):
    h, w = len(grid), len(grid[0])
    cnt = Counter(grid[r][c] for r in range(h) for c in range(w) if grid[r][c] != 0)
    bg = cnt.most_common(1)[0][0]
    out = [row[:] for row in grid]
    vis0 = [[False]*w for _ in range(h)]
    q = deque()
    for r in range(h):
        for c in range(w):
            if (r in (0, h-1) or c in (0, w-1)) and grid[r][c] == 0 and not vis0[r][c]:
                vis0[r][c] = True
                q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 0 and not vis0[nr][nc]:
                vis0[nr][nc] = True
                q.append((nr, nc))
    hole_cells = {(r,c) for r in range(h) for c in range(w) if grid[r][c]==0 and not vis0[r][c]}
    holes = []
    seen = set()
    for cell in hole_cells:
        if cell in seen: continue
        comp = []
        q = deque([cell])
        seen.add(cell)
        while q:
            r, c = q.popleft()
            comp.append((r,c))
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if (nr,nc) in hole_cells and (nr,nc) not in seen:
                    seen.add((nr,nc))
                    q.append((nr,nc))
        holes.append(comp)
    vis = [[False]*w for _ in range(h)]
    clusters = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 0 and grid[r][c] != bg and not vis[r][c]:
                col = grid[r][c]
                comp = []
                q = deque([(r,c)])
                vis[r][c] = True
                while q:
                    rr, cc = q.popleft()
                    comp.append((rr,cc))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < h and 0 <= nc < w and not vis[nr][nc] and grid[nr][nc]==col:
                            vis[nr][nc] = True
                            q.append((nr,nc))
                clusters.append((col, comp))
    def normalize(comp):
        rs = [r for r,c in comp]; cs = [c for r,c in comp]
        mr, mc = min(rs), min(cs)
        shape = frozenset((r-mr, c-mc) for r,c in comp)
        return shape, mr, mc
    hole_map = {}
    for comp in holes:
        shape, hr, hc = normalize(comp)
        hole_map.setdefault(shape, []).append((comp, hr, hc))
    cluster_map = {}
    for col, comp in clusters:
        shape, mr, mc = normalize(comp)
        cluster_map.setdefault(shape, []).append((col, comp, mr, mc))
    for shape in list(cluster_map):
        if shape in hole_map:
            while cluster_map[shape] and hole_map[shape]:
                col, comp, mr, mc = cluster_map[shape].pop(0)
                hcomp, hr, hc = hole_map[shape].pop(0)
                for r,c in comp:
                    out[r][c] = 0
                dr, dc = hr-mr, hc-mc
                for r,c in comp:
                    out[r+dr][c+dc] = col
    return out