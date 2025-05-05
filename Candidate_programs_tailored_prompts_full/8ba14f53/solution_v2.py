def solve(grid):
    h, w = len(grid), len(grid[0])
    boxes = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v:
                if v not in boxes:
                    boxes[v] = [i, i, j, j]
                else:
                    boxes[v][0] = min(boxes[v][0], i)
                    boxes[v][1] = max(boxes[v][1], i)
                    boxes[v][2] = min(boxes[v][2], j)
                    boxes[v][3] = max(boxes[v][3], j)
    cols = sorted(boxes.items(), key=lambda x: x[1][2])
    (c1, b1), (c2, b2) = cols
    w1 = min(b1[3] - b1[2] + 1, 3)
    h2 = min(b2[1] - b2[0] + 1, 3)
    out = [[0]*3 for _ in range(3)]
    for x in range(w1):
        out[0][x] = c1
    for x in range(h2):
        out[1][x] = c2
    return out