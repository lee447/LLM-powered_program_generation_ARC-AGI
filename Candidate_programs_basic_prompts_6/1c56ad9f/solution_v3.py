def solve(grid):
    h, w = len(grid), len(grid[0])
    C = None
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0:
                C = grid[i][j]
                break
        if C is not None:
            break
    min_r = h
    max_r = -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] == C:
                if i < min_r: min_r = i
                if i > max_r: max_r = i
    shift_map = {0: 0, 1: -1, 2: 0, 3: 1}
    out = [[0]*w for _ in range(h)]
    for i in range(min_r, max_r+1):
        if i == min_r or i == max_r:
            shift = 0
        else:
            shift = shift_map[(i-min_r) % 4]
        for j in range(w):
            if grid[i][j] == C:
                nj = j + shift
                if 0 <= nj < w:
                    out[i][nj] = C
    return out