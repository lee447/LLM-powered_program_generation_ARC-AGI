from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    r0, r1 = H, -1
    c0, c1 = W, -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 4:
                r0 = min(r0, i)
                r1 = max(r1, i)
                c0 = min(c0, j)
                c1 = max(c1, j)
    h, w = r1 - r0 + 1, c1 - c0 + 1
    tile = [row[c0:c0+w] for row in grid[r0:r0+h]]
    newH, newW = 3*h, 3*w
    out = [[0]*newW for _ in range(newH)]
    for dr, dc in ((0,1),(1,0),(1,2),(2,1)):
        for i in range(h):
            for j in range(w):
                out[dr*h + i][dc*w + j] = tile[i][j]
    return out