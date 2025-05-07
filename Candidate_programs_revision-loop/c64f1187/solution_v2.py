def solve(grid):
    r0 = min(r for r, row in enumerate(grid) if 5 in row)
    r1 = max(r for r, row in enumerate(grid) if 5 in row)
    c0 = min(c for c in range(len(grid[0])) if any(row[c] == 5 for row in grid))
    c1 = max(c for c in range(len(grid[0])) if any(row[c] == 5 for row in grid))
    region = [row[c0:c1+1] for row in grid[r0:r1+1]]
    H, W = len(region), len(region[0])
    BH = 2; SH = 1
    BW = 2; SW = 1
    br = (H + SH) // (BH + SH)
    bc = (W + SW) // (BW + SW)
    out = [[0]*W for _ in range(H)]
    for bi in range(br):
        for bj in range(bc):
            rs = bi*(BH+SH)
            cs = bj*(BW+SW)
            color = None
            for i in range(BH):
                for j in range(BW):
                    v = region[rs+i][cs+j]
                    if v and v != 5:
                        color = v
            if color is None:
                continue
            for i in range(BH):
                for j in range(BW):
                    if region[rs+i][cs+j] == 5:
                        out[rs+i][cs+j] = color
    return out