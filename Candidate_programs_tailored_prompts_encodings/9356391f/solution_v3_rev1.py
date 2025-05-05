from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    palette = []
    for v in grid[0]:
        if v == 0:
            break
        palette.append(v)
    marker_color = None
    marker_col = None
    for j in range(len(palette), W):
        v = grid[0][j]
        if v != 0:
            marker_color = v
            marker_col = j
            break
    if marker_color is None or marker_color == palette[-1]:
        return [row[:] for row in grid]
    bg = grid[1][marker_col]
    out = [row[:] for row in grid]
    out[0][marker_col] = bg
    min_r = H; max_r = -1; min_c = W; max_c = -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == marker_color:
                if i < min_r: min_r = i
                if i > max_r: max_r = i
                if j < min_c: min_c = j
                if j > max_c: max_c = j
    cr = (min_r + max_r) // 2
    cc = (min_c + max_c) // 2
    r = (max_r - min_r) // 2
    rings = [marker_color] + palette[::-1]
    for i in range(min_r, max_r+1):
        for j in range(min_c, max_c+1):
            out[i][j] = 0
    for t, col in enumerate(rings):
        rad = r - t
        r1, r2 = cr - rad, cr + rad
        c1, c2 = cc - rad, cc + rad
        for j in range(c1, c2+1):
            out[r1][j] = col
            out[r2][j] = col
        for i in range(r1, r2+1):
            out[i][c1] = col
            out[i][c2] = col
    return out