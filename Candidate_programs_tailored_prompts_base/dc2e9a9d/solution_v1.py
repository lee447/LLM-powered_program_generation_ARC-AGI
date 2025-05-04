def solve(grid):
    h = len(grid)
    w = len(grid[0])
    anchors = []
    for i in range(h - 4):
        for j in range(w - 4):
            ok = True
            for d in range(5):
                if grid[i + d][j] != 3 or grid[i + d][j + 4] != 3 or grid[i][j + d] != 3 or grid[i + 4][j + d] != 3:
                    ok = False
                    break
            if not ok:
                continue
            for di in range(1, 4):
                for dj in range(1, 4):
                    if grid[i + di][j + dj] != 0:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                anchors.append((i, j))
    anchors.sort(key=lambda x: x[0])
    out = [row[:] for row in grid]
    for idx, (i, j) in enumerate(anchors):
        color = 1 if idx < len(anchors) - 1 else 8
        for di in range(1, 4):
            for dj in range(1, 4):
                out[i + di][j + dj] = color
    return out