def solve(grid):
    n, m = len(grid), len(grid[0])
    from collections import defaultdict
    best_c, best_area = None, 0
    for c in set(sum(grid, [])):
        coords = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == c]
        if len(coords) <= 1: continue
        rs = [i for i, _ in coords]; cs = [j for _, j in coords]
        r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
        if (r1 - r0 + 1) * (c1 - c0 + 1) == len(coords):
            area = len(coords)
            if area > best_area:
                best_area = area
                best_c = c
                br0, br1, bc0, bc1 = r0, r1, c0, c1
    h, w = br1 - br0 + 1, bc1 - bc0 + 1
    freq = defaultdict(int)
    shapes = {}
    for i in range(n - h + 1):
        for j in range(m - w + 1):
            block = tuple(tuple(grid[i + di][j + dj] for dj in range(w)) for di in range(h))
            if any(best_c == cell for row in block for cell in row): continue
            freq[block] += 1
            shapes[block] = block
    motif = max(freq, key=freq.get)
    return [list(row) for row in motif]