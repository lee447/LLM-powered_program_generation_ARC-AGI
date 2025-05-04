from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    minr, minc, maxr, maxc = h, w, -1, -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0:
                if i < minr: minr = i
                if i > maxr: maxr = i
                if j < minc: minc = j
                if j > maxc: maxc = j
    hbox = maxr - minr + 1
    wbox = maxc - minc + 1
    size = hbox if hbox > wbox else wbox
    dr = size - hbox
    top = dr // 2
    bottom = dr - top
    new_minr = minr - top
    new_maxr = maxr + bottom
    dc = size - wbox
    left = dc // 2
    right = dc - left
    new_minc = minc - left
    new_maxc = maxc + right
    if new_minr < 0:
        new_maxr += -new_minr
        new_minr = 0
    if new_maxr >= h:
        new_minr -= new_maxr - (h - 1)
        new_maxr = h - 1
    if new_minc < 0:
        new_maxc += -new_minc
        new_minc = 0
    if new_maxc >= w:
        new_minc -= new_maxc - (w - 1)
        new_maxc = w - 1
    half = size // 2
    return [[grid[new_minr + i][new_minc + j] for j in range(half)] for i in range(half)]