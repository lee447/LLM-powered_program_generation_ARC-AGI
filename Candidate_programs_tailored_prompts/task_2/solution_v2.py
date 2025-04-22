def solve(grid):
    cl_dict = {}
    for i,row in enumerate(grid):
        for j,v in enumerate(row):
            if v:
                cl_dict.setdefault(v, []).append((i,j))
    items = list(cl_dict.items())
    cluster = min(items, key=lambda x: len(x[1]))[0]
    lines = [(c,coords) for c,coords in items if c!=cluster]
    lines.sort(key=lambda x: len(x[1]), reverse=True)
    frames = [c for c,_ in lines]
    fcount = len(frames)
    n = len(cl_dict[frames[0]])
    out = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            d = min(i, j, n-1-i, n-1-j)
            out[i][j] = frames[d] if d<fcount else cluster
    return out