from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    w = cols // 3
    cnt = [0]*3
    for z in range(3):
        for r in range(rows):
            for c in range(z*w, z*w+w):
                if grid[r][c] == 5:
                    cnt[z] += 1
    ranks = sorted(range(3), key=lambda i: cnt[i], reverse=True)
    palette = sorted({v for row in grid for v in row if v not in (0,5)})
    if len(palette) < 3:
        palette = sorted(set(range(1,10)) - {0,5})[:3]
    cmap = {}
    for i, z in enumerate(ranks):
        cmap[z] = palette[i]
    out = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            out[r][c] = cmap[c//w]
    return out