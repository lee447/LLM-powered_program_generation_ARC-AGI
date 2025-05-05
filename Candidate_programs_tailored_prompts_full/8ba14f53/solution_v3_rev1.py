from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
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
    lh = lb[1] - lb[0] + 1
    rh = rb[1] - rb[0] + 1
    total = lh + rh
    f1 = 3 * lh / total
    f2 = 3 * rh / total
    r1 = int(f1)
    r2 = int(f2)
    rem = 3 - (r1 + r2)
    frac1 = f1 - r1
    frac2 = f2 - r2
    for _ in range(rem):
        if frac1 >= frac2:
            r1 += 1
            frac1 = 0
        else:
            r2 += 1
            frac2 = 0
    out = [[0]*3 for _ in range(3)]
    row = 0
    for _ in range(r1):
        for c in range(3):
            out[row][c] = lc
        row += 1
    for _ in range(r2):
        for c in range(3):
            out[row][c] = rc
        row += 1
    return out