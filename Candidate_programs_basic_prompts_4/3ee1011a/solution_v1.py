def solve(grid):
    coords = {}
    for y,row in enumerate(grid):
        for x,val in enumerate(row):
            if val!=0:
                coords.setdefault(val,[]).append((x,y))
    bars = sorted(((len(v),k) for k,v in coords.items()), reverse=True)
    size = bars[0][0]
    res = [[0]*size for _ in range(size)]
    for i,(_,c) in enumerate(bars):
        for x in range(i, size-i):
            res[i][x] = c
            res[size-1-i][x] = c
        for y in range(i+1, size-1-i):
            res[y][i] = c
            res[y][size-1-i] = c
    return res