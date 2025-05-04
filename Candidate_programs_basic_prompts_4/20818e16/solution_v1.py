from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    minr, maxr, minc, maxc = h, -1, w, -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] != bg:
                if i < minr: minr = i
                if i > maxr: maxr = i
                if j < minc: minc = j
                if j > maxc: maxc = j
    sub = [row[minc:maxc+1] for row in grid[minr:maxr+1]]
    sh, sw = len(sub), len(sub[0])
    rot = [[sub[sh-1-r][i] for r in range(sh)] for i in range(sw)]
    h2, w2 = len(rot), len(rot[0])
    minr2, maxr2, minc2, maxc2 = h2, -1, w2, -1
    for i in range(h2):
        for j in range(w2):
            if rot[i][j] != bg:
                if i < minr2: minr2 = i
                if i > maxr2: maxr2 = i
                if j < minc2: minc2 = j
                if j > maxc2: maxc2 = j
    return [row[minc2:maxc2+1] for row in rot[minr2:maxr2+1]]