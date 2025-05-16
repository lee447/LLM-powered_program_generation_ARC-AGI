def solve(grid):
    h, w = len(grid), len(grid[0])
    bg, sep, fill = 8, 6, 3
    out = [row[:] for row in grid]
    is_cont = [any(grid[i][j] not in (bg, sep) for j in range(w)) for i in range(h)]
    i = 0
    row_runs = []
    while i < h:
        if is_cont[i]:
            s = i
            while i < h and is_cont[i]:
                i += 1
            row_runs.append((s, i - 1))
        i += 1
    for rs, re in row_runs:
        if re - rs != 2:
            continue
        mask = [any(grid[r][c] not in (bg, sep) for r in range(rs, re + 1)) for c in range(w)]
        j = 0
        while j < w:
            if mask[j]:
                cs = j
                while j < w and mask[j]:
                    j += 1
                ce = j - 1
                if ce - cs == 2:
                    for rr in range(rs - 1, re + 2):
                        for cc in range(cs - 1, ce + 2):
                            if 0 <= rr < h and 0 <= cc < w:
                                if not (rs <= rr <= re and cs <= cc <= ce) and out[rr][cc] == bg:
                                    out[rr][cc] = fill
            else:
                j += 1
    return out