def solve(grid):
    rows, cols = len(grid), len(grid[0])
    out = [[0]*cols for _ in range(rows)]
    # process row0
    run_end = 0
    while run_end < cols and grid[0][run_end] != 0:
        run_end += 1
    run0 = grid[0][:run_end]
    # compress consecutive duplicates
    palette = []
    prev = None
    for v in run0:
        if v != prev:
            palette.append(v)
            prev = v
    # detect stray pixel
    stray = None
    for j in range(run_end, cols):
        if grid[0][j] != 0:
            stray = grid[0][j]
            out[0][j] = 5
    if stray is not None:
        palette.append(stray)
    # fill out row0
    for j in range(run_end):
        out[0][j] = grid[0][j]
    # copy row1
    if rows > 1:
        out[1] = list(grid[1])
    # find marker
    center = None
    for i in range(2, rows):
        for j in range(cols):
            if grid[i][j] != 0:
                center = (i, j)
                break
        if center:
            break
    if center:
        cr, cc = center
        # draw rings
        for idx, color in enumerate(palette):
            half = idx
            top, left = cr-half, cc-half
            bot, right = cr+half, cc+half
            if half == 0:
                if 0 <= cr < rows and 0 <= cc < cols:
                    out[cr][cc] = color
            else:
                for x in range(left, right+1):
                    if 0 <= top < rows and 0 <= x < cols:
                        out[top][x] = color
                    if 0 <= bot < rows and 0 <= x < cols:
                        out[bot][x] = color
                for y in range(top, bot+1):
                    if 0 <= y < rows and 0 <= left < cols:
                        out[y][left] = color
                    if 0 <= y < rows and 0 <= right < cols:
                        out[y][right] = color
    return out