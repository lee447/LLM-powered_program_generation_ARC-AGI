def solve(grid):
    h, w = len(grid), len(grid[0])
    order = []
    seen = set()
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != 0 and c not in seen:
                seen.add(c)
                order.append(c)
    boxes = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != 0:
                if c not in boxes:
                    boxes[c] = [i, i, j, j]
                else:
                    r0, r1, c0, c1 = boxes[c]
                    boxes[c] = [min(r0, i), max(r1, i), min(c0, j), max(c1, j)]
    out = [row[:] for row in grid]
    for c in reversed(order):
        r0, r1, c0, c1 = boxes[c]
        for i in range(r0, r1 + 1):
            for j in range(c0, c1 + 1):
                out[i][j] = c
    return out