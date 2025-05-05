def solve(grid):
    H, W = len(grid), len(grid[0])
    row_colors = []
    for row in grid:
        cs = {x for x in row if x}
        row_colors.append(cs.pop() if len(cs) == 1 else None)
    out = [[0]*W for _ in range(H)]
    i = 0
    while i < H:
        if row_colors[i] is None:
            i += 1
            continue
        c = row_colors[i]
        s = i
        j = i + 1
        while j < H and row_colors[j] == c:
            j += 1
        e = j - 1
        for r in range(s, e+1):
            tr = s + e - r
            for col in range(W):
                if grid[r][col] == c:
                    out[tr][col] = c
        i = j
    return out