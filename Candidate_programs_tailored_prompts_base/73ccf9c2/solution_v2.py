def solve(grid):
    n = len(grid)
    m = len(grid[0])
    coords = [(i, j) for i in range(n) for j in range(m) if grid[i][j] != 0]
    coords_set = set(coords)
    visited = set()
    comps = []
    for p in coords:
        if p in visited:
            continue
        stack = [p]
        comp = []
        visited.add(p)
        while stack:
            r, c = stack.pop()
            comp.append((r, c))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    q = (r + dr, c + dc)
                    if q in coords_set and q not in visited:
                        visited.add(q)
                        stack.append(q)
        comps.append(comp)
    cluster = max(comps, key=lambda comp: sum(r + c for r, c in comp) / len(comp))
    rows = [r for r, _ in cluster]
    cols = [c for _, c in cluster]
    minr, maxr = min(rows), max(rows)
    minc, maxc = min(cols), max(cols)
    out = []
    for i in range(minr, maxr + 1):
        out.append([grid[i][j] for j in range(minc, maxc + 1)])
    return out