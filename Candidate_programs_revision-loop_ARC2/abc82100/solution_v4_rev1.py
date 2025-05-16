from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    hor = None
    ver = None
    for i in range(h):
        j = 0
        while j < w:
            c = grid[i][j]
            if c != 0:
                k = j + 1
                while k < w and grid[i][k] == c:
                    k += 1
                if k - j > 1:
                    hor = (i, j, k - j, c)
                j = k
            else:
                j += 1
    for j in range(w):
        i = 0
        while i < h:
            c = grid[i][j]
            if c != 0:
                k = i + 1
                while k < h and grid[k][j] == c:
                    k += 1
                if k - i > 1:
                    ver = (i, j, k - i, c)
                i = k
            else:
                i += 1
    out = [[0] * w for _ in range(h)]
    if hor and ver:
        ri, cj, Lh, ch = hor
        ci, rj, Lv, cv = ver
        for x in range(Lh):
            out[ri][cj + x] = cv
        for y in range(Lv):
            out[ci + y][rj] = ch
    return out