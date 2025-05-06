from typing import List, Tuple

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    counts = {}
    for r in range(h):
        for c in range(w):
            counts[grid[r][c]] = counts.get(grid[r][c], 0) + 1
    bg = max(counts, key=counts.get)
    shapes = []
    for color, cnt in counts.items():
        if color == bg: continue
        r0, r1, c0, c1 = h, -1, w, -1
        for r in range(h):
            for c in range(w):
                if grid[r][c] == color:
                    r0 = min(r0, r); r1 = max(r1, r)
                    c0 = min(c0, c); c1 = max(c1, c)
        shapes.append((cnt, color, r0, r1, c0, c1))
    shapes.sort()
    _, big, br0, br1, bc0, bc1 = shapes[-1]
    H, W = br1 - br0 + 1, bc1 - bc0 + 1
    out = [[big]*W for _ in range(H)]
    for cnt, color, r0, r1, c0, c1 in shapes[:-1]:
        h0, w0 = r1 - r0 + 1, c1 - c0 + 1
        if cnt == shapes[0][0]:
            roff, coff = 0, 0
        else:
            roff, coff = 0, shapes[0][5] - shapes[0][4] + 1
        for i in range(h0):
            for j in range(w0):
                out[roff+i][coff+j] = color
    return out