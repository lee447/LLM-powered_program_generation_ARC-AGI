import numpy as np

def solve(grid):
    H, W = len(grid), len(grid[0])
    def mode(lst):
        d = {}
        for x in lst:
            d[x] = d.get(x, 0) + 1
        m, mv = None, -1
        for x, v in d.items():
            if v > mv:
                m, mv = x, v
        return m
    run_threshold = 3
    row_flag = [False]*H
    for r in range(H):
        cnt = 0
        for c in range(W):
            if grid[r][c] != 0:
                cnt += 1
                if cnt >= run_threshold:
                    row_flag[r] = True
                    break
            else:
                cnt = 0
    blocks = []
    r = 0
    while r < H:
        if row_flag[r]:
            start = r
            while r+1 < H and row_flag[r+1]:
                r += 1
            blocks.append((start, r))
        r += 1
    new = [[0]*W for _ in range(H)]
    for (r0, r1) in blocks:
        bh = r1 - r0 + 1
        thresh = (bh+1)//2
        col_ok = [False]*W
        for c in range(W):
            cnt = sum(1 for r in range(r0, r1+1) if grid[r][c] != 0)
            col_ok[c] = cnt >= thresh
        intervals = []
        c = 0
        while c < W:
            if col_ok[c]:
                s = c
                while c+1 < W and col_ok[c+1]:
                    c += 1
                intervals.append((s, c))
            c += 1
        for (c1, c2) in intervals:
            width = c2 - c1 + 1
            valid_rows = []
            for r in range(r0, r1+1):
                cnt = sum(1 for c in range(c1, c2+1) if grid[r][c] != 0)
                if cnt == width:
                    valid_rows.append(r)
            if valid_rows:
                pr = max(valid_rows)
            else:
                pr = r1
            m0 = mode([grid[r0][c] for c in range(c1, c2+1) if grid[r0][c] != 0])
            for c in range(c1, c2+1):
                new[r0][c] = m0
            for r in range(r0+1, r1+1):
                for c in range(c1, c2+1):
                    new[r][c] = grid[pr][c]
    return new