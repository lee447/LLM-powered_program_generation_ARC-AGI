def solve(grid):
    h = len(grid)
    w = len(grid[0])
    mid = next(i for i,row in enumerate(grid) if all(x==5 for x in row))
    anchors = []
    for j in range(w):
        above = [grid[r][j] for r in range(mid) if grid[r][j] not in (0,5)]
        below = [grid[r][j] for r in range(mid+1,h) if grid[r][j] not in (0,5)]
        if above and below:
            cols = set(above+below)
            if len(cols)==1:
                c = cols.pop()
                a = len(above)
                b = len(below)
                anchors.append((c, a, b, abs(b-a)))
    if not anchors:
        return [[0,0],[0,0]]
    best = max(anchors, key=lambda x: x[3])
    color = best[0]
    return [[color, color], [color, color]]