from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    div = grid[0].index(5)
    left_w = div
    right_off = div + 1
    hole_min_r = h; hole_max_r = -1; hole_min_c = left_w; hole_max_c = -1
    for i in range(h):
        for j in range(left_w):
            if grid[i][j] == 0:
                hole_min_r = min(hole_min_r, i)
                hole_max_r = max(hole_max_r, i)
                hole_min_c = min(hole_min_c, j)
                hole_max_c = max(hole_max_c, j)
    shape_min_r = h; shape_max_r = -1; shape_min_c = w; shape_max_c = -1
    for i in range(h):
        for j in range(right_off, w):
            if grid[i][j] != 0:
                shape_min_r = min(shape_min_r, i)
                shape_max_r = max(shape_max_r, i)
                shape_min_c = min(shape_min_c, j)
                shape_max_c = max(shape_max_c, j)
    canvas = [row[:left_w] for row in grid]
    if hole_max_r >= 0 and shape_max_r >= 0:
        hole_c2 = hole_min_c + hole_max_c
        hole_r2 = hole_min_r + hole_max_r
        shape_r2 = shape_min_r + shape_max_r
        shape_c2 = (shape_min_c - right_off) + (shape_max_c - right_off)
        if hole_r2 == shape_r2 and hole_c2 == shape_c2:
            for i in range(h):
                for j in range(left_w):
                    if canvas[i][j] == 0 and grid[i][right_off + j] != 0:
                        canvas[i][j] = grid[i][right_off + j]
    return canvas