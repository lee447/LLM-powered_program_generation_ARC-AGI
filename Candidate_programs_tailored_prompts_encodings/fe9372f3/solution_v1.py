from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    core = {(i, j) for i in range(h) for j in range(w) if grid[i][j] == 2}
    cr, cc = next((i, j) for (i, j) in core if (i-1, j) in core and (i+1, j) in core and (i, j-1) in core and (i, j+1) in core)
    out = [[0]*w for _ in range(h)]
    for i, j in core:
        out[i][j] = 2
    for j in range(w):
        if (cr, j) not in core:
            d = min(abs(j - (cc-1)), abs(j - (cc+1)))
            out[cr][j] = 4 if d % 3 == 0 else 8
    for i in range(h):
        if (i, cc) not in core:
            d = min(abs(i - (cr-1)), abs(i - (cr+1)))
            out[i][cc] = 4 if d % 3 == 0 else 8
    k = 1
    while cr-k >= 0 and cc-k >= 0:
        out[cr-k][cc-k] = 1; k += 1
    k = 1
    while cr-k >= 0 and cc+k < w:
        out[cr-k][cc+k] = 1; k += 1
    k = 1
    while cr+k < h and cc-k >= 0:
        out[cr+k][cc-k] = 1; k += 1
    k = 1
    while cr+k < h and cc+k < w:
        out[cr+k][cc+k] = 1; k += 1
    return out