def solve(grid):
    w = len(grid[0])
    h = w
    out = [[0]*w for _ in range(h)]
    apex_col = next(c for c,v in enumerate(grid[0]) if v==2)
    # draw red V until boundary
    max_r = 0
    for i in range(w):
        l = apex_col - i
        r = apex_col + i
        if l < 0 or r >= w:
            break
        out[i][l] = 2
        out[i][r] = 2
        max_r = i
    # draw blue inverted-V inside
    for j in range(1, max_r+1):
        r = max_r + j
        if r >= h:
            break
        l = apex_col - j
        rcol = apex_col + j
        if 0 <= l < w and 0 <= rcol < w:
            out[r][l] = 1
            out[r][rcol] = 1
        elif 0 <= l < w:
            out[r][l] = 1
        elif 0 <= rcol < w:
            out[r][rcol] = 1
    return out