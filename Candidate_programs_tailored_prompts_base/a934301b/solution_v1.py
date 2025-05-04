def solve(grid):
    h, w = len(grid), len(grid[0])
    patches = []
    for i in range(h - 2):
        for j in range(w - 2):
            block = [grid[i + di][j + dj] for di in range(3) for dj in range(3)]
            if all(c in (1, 8) for c in block) and block.count(8) == 1:
                patches.append((i, j))
    if not patches:
        return [[0]*w for _ in range(h)]
    rows = sorted({i for i, _ in patches})
    counts = {r: sum(1 for i,_ in patches if i==r) for r in rows}
    cutoff = max(r for r,c in counts.items() if c == max(counts.values()))
    keep = []
    byrow = {}
    for i,j in patches:
        if i <= cutoff:
            byrow.setdefault(i, []).append(j)
    for i, js in byrow.items():
        keep.append((i, max(js)))
    out = [[0]*w for _ in range(h)]
    for i,j in keep:
        for di in range(3):
            for dj in range(3):
                if grid[i+di][j+dj] in (1,8):
                    out[i+di][j+dj] = grid[i+di][j+dj]
    return out