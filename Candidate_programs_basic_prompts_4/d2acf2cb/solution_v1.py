from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    shape_color = 6
    background_color = 0
    pattern_shape = shape_color + 1
    pattern_background = shape_color + 2
    frames = []
    for i in range(1, h-1):
        pts = [j for j in range(w) if grid[i][j] == 4]
        if len(pts) == 2:
            c1, c2 = pts
            if c2 - c1 > 1:
                frames.append(("h", i, c1+1, c2))
    for j in range(1, w-1):
        pts = [i for i in range(h) if grid[i][j] == 4]
        if len(pts) == 2:
            r1, r2 = pts
            if r2 - r1 > 1:
                frames.append(("v", j, r1+1, r2))
    mode = None
    if frames:
        ori, a, b1, b2 = frames[0]
        vals = set()
        if ori == "h":
            for j in range(b1, b2):
                vals.add(grid[a][j])
        else:
            for i in range(b1, b2):
                vals.add(grid[i][a])
        if vals <= {0, shape_color}:
            mode = "paint"
        else:
            mode = "erase"
    res = [row[:] for row in grid]
    for ori, a, b1, b2 in frames:
        if ori == "h":
            i = a
            for j in range(b1, b2):
                v = grid[i][j]
                if mode == "paint":
                    if v == shape_color:
                        res[i][j] = pattern_shape
                    elif v == background_color:
                        res[i][j] = pattern_background
                else:
                    if v == pattern_shape:
                        res[i][j] = shape_color
                    elif v == pattern_background:
                        res[i][j] = background_color
        else:
            j = a
            for i in range(b1, b2):
                v = grid[i][j]
                if mode == "paint":
                    if v == shape_color:
                        res[i][j] = pattern_shape
                    elif v == background_color:
                        res[i][j] = pattern_background
                else:
                    if v == pattern_shape:
                        res[i][j] = shape_color
                    elif v == pattern_background:
                        res[i][j] = background_color
    return res