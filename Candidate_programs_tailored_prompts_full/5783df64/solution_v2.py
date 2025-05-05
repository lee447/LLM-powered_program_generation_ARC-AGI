def solve(grid):
    h = len(grid)
    band_h = h // 3
    bands = [[] for _ in range(3)]
    for r, row in enumerate(grid):
        b = min(r // band_h, 2)
        for c, v in enumerate(row):
            if v != 0:
                bands[b].append((c, v))
    output = []
    for band in bands:
        band.sort(key=lambda x: x[0])
        output.append([v for _, v in band])
    return output