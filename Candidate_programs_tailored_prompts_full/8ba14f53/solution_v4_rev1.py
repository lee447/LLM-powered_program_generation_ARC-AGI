from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
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
    h1 = b1[1] - b1[0] + 1
    w2 = b2[3] - b2[2] + 1
    k1 = 3 if h1 > 3 else 1
    k2 = 3 if w2 > 4 else w2 - 1
    out = [[0]*3 for _ in range(3)]
    for x in range(k1):
        out[0][x] = c1
    for x in range(k2):
        out[1][x] = c2
    return out