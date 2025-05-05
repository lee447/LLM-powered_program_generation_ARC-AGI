def solve(grid):
    h, w = len(grid), len(grid[0])
    boxes = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v:
                if v not in boxes:
                    boxes[v] = [r, r, c, c]
                else:
                    boxes[v][0] = min(boxes[v][0], r)
                    boxes[v][1] = max(boxes[v][1], r)
                    boxes[v][2] = min(boxes[v][2], c)
                    boxes[v][3] = max(boxes[v][3], c)
    items = sorted(boxes.items(), key=lambda x: x[1][2])
    (lc, lb), (rc, rb) = items[0], items[1]
    lminr, lmaxr, lminc, lmaxc = lb
    rminr, rmaxr, rminc, rmaxc = rb
    left_span = min(3, lmaxc - lminc + 1)
    right_span = min(3, rmaxr - rminr + 1)
    out = [[0,0,0] for _ in range(3)]
    for i in range(left_span):
        out[0][i] = lc
    for i in range(right_span):
        out[1][i] = rc
    return out