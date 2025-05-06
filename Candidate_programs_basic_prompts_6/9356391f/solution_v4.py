from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    v_header = []
    for j in range(w):
        if grid[0][j] != 0:
            v_header.append(grid[0][j])
        else:
            break
    r1 = len(v_header) - 1
    r2 = None
    h_color = None
    for j in range(len(v_header), w):
        if grid[0][j] != 0:
            r2 = j
            h_color = grid[0][j]
            break
    ci = cj = None
    target = v_header[0]
    for i in range(1, h):
        for j in range(w):
            if grid[i][j] == target:
                ci, cj = i, j
                break
        if ci is not None:
            break
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            dv = abs(i - ci)
            dh = abs(j - cj)
            d = dv if dv > dh else dh
            if r2 is not None and d == r2:
                out[i][j] = h_color
            elif d <= r1:
                out[i][j] = v_header[d]
    return out