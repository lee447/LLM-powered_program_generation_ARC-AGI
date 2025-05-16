from collections import Counter, deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    cnt = Counter(cell for row in grid for cell in row)
    bg = cnt.most_common(1)[0][0]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def comps(color):
        seen = [[False]*w for _ in range(h)]
        out = []
        for i in range(h):
            for j in range(w):
                if not seen[i][j] and grid[i][j] == color:
                    q = deque([(i,j)])
                    seen[i][j] = True
                    comp = []
                    while q:
                        x, y = q.popleft()
                        comp.append((x,y))
                        for dx,dy in dirs:
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and grid[nx][ny] == color:
                                seen[nx][ny] = True
                                q.append((nx,ny))
                    out.append(comp)
        return out
    colors = [c for c in cnt if c != bg]
    cd = {c: comps(c) for c in colors}
    color_A = next(c for c in colors if len(cd[c])==2 and len(cd[c][0])==len(cd[c][1]))
    color_B = next(c for c in colors if c != color_A)
    comps_A = cd[color_A]
    comps_B = cd[color_B]
    comps_B.sort(key=lambda x: len(x), reverse=True)
    shape = comps_B[0]
    minr = min(r for r,c in shape)
    minc = min(c for r,c in shape)
    rel = [(r-minr,c-minc) for r,c in shape]
    orients = []
    for rot in range(4):
        cur = []
        for r,c in rel:
            rr, cc = r, c
            for _ in range(rot):
                rr, cc = cc, -rr
            cur.append((rr,cc))
        mr = min(r for r,c in cur)
        mc = min(c for r,c in cur)
        norm = tuple(sorted(((r-mr,c-mc) for r,c in cur)))
        if norm not in orients:
            orients.append(norm)
    new_color = 2
    used = set()
    for compA in comps_A:
        sA = set(compA)
        placed = False
        for orient in orients:
            orient = list(orient)
            for qr,qc in orient:
                for px,py in compA:
                    for dx,dy in dirs:
                        off_r = px + dx - qr
                        off_c = py + dy - qc
                        placed_coords = [(off_r+r, off_c+c) for r,c in orient]
                        ok = True
                        for rr,cc in placed_coords:
                            if not (0<=rr<h and 0<=cc<w) or (grid[rr][cc] != bg and grid[rr][cc] != color_B):
                                ok = False
                                break
                        if not ok:
                            continue
                        adj = 0
                        for rr,cc in placed_coords:
                            for dx2,dy2 in dirs:
                                if (rr+dx2,cc+dy2) in sA:
                                    adj += 1
                        if adj != 1:
                            continue
                        adj_cell = (off_r+qr, off_c+qc)
                        if adj_cell in used:
                            continue
                        for rr,cc in placed_coords:
                            grid[rr][cc] = new_color if (rr,cc)==adj_cell else color_B
                        used.add(adj_cell)
                        placed = True
                        break
                    if placed:
                        break
                if placed:
                    break
            if placed:
                break
    return grid