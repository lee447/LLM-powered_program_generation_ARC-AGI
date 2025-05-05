def solve(grid):
    h = len(grid)
    w = len(grid[0])
    gray = 5
    zones = []
    used = [False]*w
    for c in range(w):
        if any(grid[r][c]==gray for r in range(h)):
            if c>0 and zones and zones[-1][ -1 ]==c-1:
                zones[-1].append(c)
            else:
                zones.append([c])
    counts = [sum(1 for r in range(h) for c in z if grid[r][c]==gray) for z in zones]
    colors = sorted({grid[r][c] for r in range(h) for c in range(w) if grid[r][c]!=0 and grid[r][c]!=gray})
    if len(colors)!=len(zones):
        # fallback: pick first N positive colors not in {0,gray}
        allc = [i for i in range(1,10) if i!=gray]
        colors = allc[:len(zones)]
    order = sorted(range(len(zones)), key=lambda i: counts[i], reverse=True)
    assign = {}
    for k,i in enumerate(order):
        assign[i] = colors[k]
    out = [[0]*w for _ in range(h)]
    for i,z in enumerate(zones):
        c = assign[i]
        for r in range(h):
            for col in z:
                out[r][col] = c
    return out