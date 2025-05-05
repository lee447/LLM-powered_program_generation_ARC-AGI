from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    boxes = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0:
                if v not in boxes:
                    boxes[v] = [r, c, r, c]
                else:
                    b = boxes[v]
                    b[0] = min(b[0], r)
                    b[1] = min(b[1], c)
                    b[2] = max(b[2], r)
                    b[3] = max(b[3], c)
    out = [row[:] for row in grid]
    for v, (r0, c0, r1, c1) in boxes.items():
        for rr in range(r0, r1 + 1):
            for cc in range(c0, c1 + 1):
                out[rr][cc] = v
    return out