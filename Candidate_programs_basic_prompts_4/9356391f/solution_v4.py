def solve(grid):
    h = len(grid)
    w = len(grid[0])
    arr = grid[0]
    cx = cy = None
    for i in range(2, h):
        for j in range(w):
            if grid[i][j] != 0:
                cx, cy = i, j
                break
        if cx is not None:
            break
    res = [row[:] for row in grid]
    for j, color in enumerate(arr):
        if color == 0:
            continue
        top = cx - j
        bot = cx + j
        left = cy - j
        right = cy + j
        for x in range(left, right + 1):
            if 0 <= top < h and 0 <= x < w:
                res[top][x] = color
            if 0 <= bot < h and 0 <= x < w:
                res[bot][x] = color
        for y in range(top, bot + 1):
            if 0 <= y < h and 0 <= left < w:
                res[y][left] = color
            if 0 <= y < h and 0 <= right < w:
                res[y][right] = color
    return res