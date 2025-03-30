from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    bg = 0
    rmin, rmax = h, -1
    cmin, cmax = w, -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] != bg:
                rmin = min(rmin, i)
                rmax = max(rmax, i)
                cmin = min(cmin, j)
                cmax = max(cmax, j)
    if rmax == -1:
        return grid
    candidate_h = (h - 1) // 2
    candidate_v = (w - 1) // 2
    use_horizontal = False
    use_vertical = False
    if rmin <= candidate_h <= rmax:
        gap = True
        for j in range(cmin, cmax + 1):
            if grid[candidate_h][j] != bg:
                gap = False
                break
        if gap:
            use_horizontal = True
    if not use_horizontal and cmin <= candidate_v <= cmax:
        gap = True
        for i in range(rmin, rmax + 1):
            if grid[i][candidate_v] != bg:
                gap = False
                break
        if gap:
            use_vertical = True
    if use_horizontal:
        for j in range(w):
            grid[candidate_h][j] = 3
    elif use_vertical:
        for i in range(h):
            grid[i][candidate_v] = 3
    return grid