def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    # find stripe columns (where bottom row has nonzero)
    stripe_cols = [j for j in range(w) if grid[-1][j] != 0]
    for j in stripe_cols:
        # collect anchors in this column
        anchors = [(i, grid[i][j]) for i in range(h) if grid[i][j] != 0]
        anchors.sort(key=lambda x: x[0])
        # collapse consecutive same-color anchors
        grouped = []
        for r, c in anchors:
            if not grouped or grouped[-1][1] != c:
                grouped.append([r, c])
            else:
                grouped[-1][0] = r
        anchors = grouped
        # forward fill
        fwd = [0]*h
        if anchors:
            cur = anchors[0][1]
            r0 = anchors[0][0]
            for r in range(r0+1):
                fwd[r] = cur
            idx = 0
            for r in range(r0+1, h):
                if idx+1 < len(anchors) and r == anchors[idx+1][0]:
                    idx += 1
                    cur = anchors[idx][1]
                fwd[r] = cur
        # backward fill
        bwd = [0]*h
        if anchors:
            cur = anchors[-1][1]
            rl = anchors[-1][0]
            for r in range(h-1, rl-1, -1):
                bwd[r] = cur
            idx = len(anchors)-1
            for r in range(rl-1, -1, -1):
                if idx-1 >= 0 and r == anchors[idx-1][0]:
                    idx -= 1
                    cur = anchors[idx][1]
                bwd[r] = cur
        # merge
        for i in range(h):
            if grid[i][j] != 0:
                res[i][j] = grid[i][j]
            else:
                if fwd[i] == bwd[i]:
                    res[i][j] = fwd[i]
                else:
                    # decide based on proximity to first/last anchor
                    if i <= anchors[0][0]:
                        res[i][j] = anchors[0][1]
                    elif i >= anchors[-1][0]:
                        res[i][j] = anchors[-1][1]
                    else:
                        # find enclosing anchors
                        for k in range(len(anchors)-1):
                            if anchors[k][0] < i < anchors[k+1][0]:
                                # if it's the last interior gap use backward, else forward
                                if k+1 == len(anchors)-1:
                                    res[i][j] = anchors[k+1][1]
                                else:
                                    res[i][j] = anchors[k][1]
                                break
    return res