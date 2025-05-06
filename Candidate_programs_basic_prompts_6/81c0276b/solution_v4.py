def solve(grid):
    R, C = len(grid), len(grid[0])
    # find separator color
    sep = None
    for r in range(R):
        row = grid[r]
        v = row[0]
        if v != 0 and all(x == v for x in row):
            sep = v
            break
    # find sep rows and cols
    sep_rows = [r for r in range(R) if all(grid[r][c] == sep for c in range(C))]
    sep_cols = [c for c in range(C) if all(grid[r][c] == sep for r in range(R))]
    # build cell intervals
    def intervals(seps, N):
        ints = []
        prev = -1
        for s in seps:
            if s - prev > 1:
                ints.append((prev+1, s-1))
            prev = s
        if N-1 - prev >= 0:
            ints.append((prev+1, N-1))
        return ints
    row_ints = intervals(sep_rows, R)
    col_ints = intervals(sep_cols, C)
    # collect shapes
    shapes = set()
    cell = []
    for ri, rint in enumerate(row_ints):
        crow = []
        for ci, cint in enumerate(col_ints):
            v = 0
            for r in range(rint[0], rint[1]+1):
                for c in range(cint[0], cint[1]+1):
                    x = grid[r][c]
                    if x != 0 and x != sep:
                        v = x
            crow.append(v)
            if v:
                shapes.add(v)
        cell.append(crow)
    # sort shapes ascending
    S = sorted(shapes)
    R2 = len(S)
    C2 = len(col_ints)
    out = [[0]*C2 for _ in range(R2)]
    for i in range(R2):
        for j in range(min(i+1, C2)):
            out[i][j] = S[i]
    return out