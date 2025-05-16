from collections import deque, Counter

def solve(grid):
    h, w = len(grid), len(grid[0])
    cnt = Counter(cell for row in grid for cell in row if cell)
    bg = max(cnt, key=cnt.get)
    bg_coords = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == bg]
    min_r_bg = min(r for r, c in bg_coords)
    max_r_bg = max(r for r, c in bg_coords)
    min_c_bg = min(c for r, c in bg_coords)
    max_c_bg = max(c for r, c in bg_coords)
    hole_coords = {(r, c) for r in range(min_r_bg, max_r_bg + 1)
                   for c in range(min_c_bg, max_c_bg + 1)
                   if grid[r][c] == 0}
    holes = []
    seen = set()
    for start in hole_coords:
        if start in seen: continue
        q = deque([start])
        comp = [start]
        seen.add(start)
        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if (nr, nc) in hole_coords and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append((nr, nc))
                    comp.append((nr, nc))
        holes.append(comp)
    vis = [[False]*w for _ in range(h)]
    clusters = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] and grid[r][c] != bg and not vis[r][c]:
                col = grid[r][c]
                q = deque([(r, c)])
                comp = [(r, c)]
                vis[r][c] = True
                while q:
                    rr, cc = q.popleft()
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < h and 0 <= nc < w and not vis[nr][nc] and grid[nr][nc] == col:
                            vis[nr][nc] = True
                            q.append((nr, nc))
                            comp.append((nr, nc))
                clusters.append((col, comp))
    out = [row[:] for row in grid]
    for _, comp in clusters:
        for r, c in comp:
            out[r][c] = 0
    def normalize(comp):
        rs = [r for r, c in comp]; cs = [c for r, c in comp]
        mr, mc = min(rs), min(cs)
        shape = tuple(sorted((r-mr, c-mc) for r, c in comp))
        return shape, mr, mc
    norm_map = {}
    for col, comp in clusters:
        shape, mr, mc = normalize(comp)
        norm_map.setdefault(shape, []).append((col, comp, mr, mc))
    for hole in holes:
        shape, hr, hc = normalize(hole)
        if shape not in norm_map or not norm_map[shape]:
            continue
        col, comp, mr, mc = norm_map[shape].pop(0)
        dr, dc = hr - mr, hc - mc
        for r, c in comp:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 0:
                out[nr][nc] = col
    return out