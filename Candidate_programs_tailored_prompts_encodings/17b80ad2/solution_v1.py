def solve(grid):
    m, n = len(grid), len(grid[0])
    new = [row[:] for row in grid]
    anchors = {}
    for i in range(m):
        for j in range(n):
            v = grid[i][j]
            if v:
                anchors.setdefault(j, []).append((i, v))
    for j, al in anchors.items():
        if len(al) < 2:
            continue
        al.sort()
        last = -1
        for row, val in al:
            for i in range(last+1, row+1):
                new[i][j] = val
            last = row
    return new