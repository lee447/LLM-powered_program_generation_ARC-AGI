def solve(grid):
    uniq = set()
    for row in grid:
        for x in row:
            uniq.add(x)
    f = len(uniq)
    res = []
    for row in grid:
        t = row * f
        for _ in range(f):
            res.append(t[:])
    return res