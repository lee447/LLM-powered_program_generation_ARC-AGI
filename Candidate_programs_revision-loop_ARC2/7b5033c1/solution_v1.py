def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    freq = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            freq[v] = freq.get(v, 0) + 1
    bg = max(freq, key=lambda x: freq[x])
    info = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v == bg:
                continue
            if v not in info:
                info[v] = [1, r, c]
            else:
                info[v][0] += 1
                if r < info[v][1] or (r == info[v][1] and c < info[v][2]):
                    info[v][1], info[v][2] = r, c
    shapes = sorted([(v, cnt, mr, mc) for v, (cnt, mr, mc) in info.items()], key=lambda x: (x[2], x[3]))
    result = []
    for v, cnt, _, _ in shapes:
        for _ in range(cnt):
            result.append([v])
    return result