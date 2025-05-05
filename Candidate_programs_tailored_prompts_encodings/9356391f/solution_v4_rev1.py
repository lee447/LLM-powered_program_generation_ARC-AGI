from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    top = grid[0]
    last = max(i for i, v in enumerate(top) if v != 0)
    palette = top[: last + 1]
    # bounding box of nonzero data, excluding header rows 0 and 1
    ys = [i for i in range(2, h) if any(grid[i][j] != 0 for j in range(w))]
    xs = [j for j in range(w) if any(grid[i][j] != 0 for i in range(2, h))]
    if not ys or not xs:
        return grid
    y_min, y_max = min(ys), max(ys)
    x_min, x_max = min(xs), max(xs)
    r = len(palette) - 1
    size = 2 * r + 1
    bbox_h = y_max - y_min + 1
    bbox_w = x_max - x_min + 1
    # determine offsets
    if 0 in palette:
        y0 = y_min + 2
        x0 = x_min
    else:
        y0 = y_min + 1
        x0 = x_min + (bbox_w - size)
    # clear bounding box
    for i in range(y_min, y_max + 1):
        for j in range(x_min, x_max + 1):
            grid[i][j] = 0
    # overlay shape
    for i in range(size):
        for j in range(size):
            y = y0 + i
            x = x0 + j
            if 0 <= y < h and 0 <= x < w:
                d = max(abs(i - r), abs(j - r))
                grid[y][x] = palette[d]
    return grid