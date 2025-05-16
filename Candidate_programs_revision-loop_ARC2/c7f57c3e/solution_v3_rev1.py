from collections import Counter, deque

def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    if any(8 in row for row in grid):
        pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8]
        rmin = min(r for r, c in pts)
        cmin = min(c for r, c in pts)
        cmax = max(c for r, c in pts)
        rc = rmin - 1
        cc = (cmin + cmax) // 2
        center = grid[rc][cc]
        for r, c in pts:
            out[r][c] = center if r == rmin else center + 1
        return out
    pts4 = {(r, c) for r in range(h) for c in range(w) if grid[r][c] == 4}
    if not pts4:
        return out
    counts = Counter(grid[r][c] for r in range(h) for c in range(w))
    fill = min((c for c in counts if c != 4), key=lambda x: (counts[x], x))
    back = max(counts, key=lambda x: (counts[x], -x))
    visited = set()
    clusters = []
    for p in pts4:
        if p in visited:
            continue
        q = deque([p])
        comp = []
        visited.add(p)
        while q:
            u = q.popleft()
            comp.append(u)
            r, c = u
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                v = (r+dr, c+dc)
                if v in pts4 and v not in visited:
                    visited.add(v)
                    q.append(v)
        clusters.append(comp)
    clusters.sort(key=lambda comp: min(r for r, c in comp))
    base_r = min(r for r, c in clusters[0])
    for r, c in pts4:
        out[r][c] = back
    for comp in clusters:
        rmin = min(r for r, c in comp)
        cmin = min(c for r, c in comp)
        new_rmin = 0 if rmin == base_r else base_r
        for r, c in comp:
            dr = r - rmin
            dc = c - cmin
            rr = new_rmin + dr
            cc = cmin + dc
            if 0 <= rr < h and 0 <= cc < w:
                out[rr][cc] = fill
    return out