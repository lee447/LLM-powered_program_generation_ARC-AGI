def solve(grid):
    H = len(grid)
    W = len(grid[0])
    has6 = any(6 in row for row in grid)
    has8 = any(8 in row for row in grid)
    has1 = any(1 in row for row in grid)
    if has6:
        num6 = [row.count(6) for row in grid]
        r0 = num6.index(max(num6))
        s0 = grid[r0].index(6)
        dr = 1
        while r0 + dr < H and grid[r0 + dr][s0] != 0:
            dr += 1
        pat_h = dr
        mask = set()
        for d in range(1, pat_h):
            for c in range(W):
                if grid[r0 + d][c] != 0:
                    mask.add(c)
        pattern = [[0]*W for _ in range(pat_h)]
        for c in mask:
            pattern[0][c] = 6
        for d in range(1, pat_h):
            for c in mask:
                v = grid[r0 + d][c]
                if v != 0:
                    pattern[d][c] = v
        dr2 = 1
        while r0 + dr2 < H and grid[r0 + dr2][s0] != 6:
            dr2 += 1
        period = dr2
        out = [[0]*W for _ in range(H)]
        k = 0
        while True:
            base = r0 + k*period
            if base >= H:
                break
            for d in range(pat_h):
                r = base + d
                if r < H:
                    for c in mask:
                        v = pattern[d][c]
                        if v:
                            out[r][c] = v
            k += 1
        return out
    elif has8 and has1:
        count8 = [row.count(8) for row in grid]
        b0 = count8.index(max(count8))
        for c in range(W):
            if grid[b0][c] == 8:
                s0 = c
                break
        dr_up = 1
        while b0 - dr_up >= 0 and grid[b0 - dr_up][s0] != 0:
            dr_up += 1
        data_h = dr_up - 1
        r0 = b0 - data_h
        pat_h = data_h + 1
        mask = set()
        for d in range(pat_h):
            r = r0 + d
            if 0 <= r < H:
                for c in range(W):
                    if grid[r][c] != 0:
                        mask.add(c)
        pattern = [[0]*W for _ in range(pat_h)]
        for d in range(pat_h):
            r = r0 + d
            if 0 <= r < H:
                for c in mask:
                    v = grid[r][c]
                    if v != 0:
                        pattern[d][c] = v
        seed = grid[r0][s0]
        dr2 = 1
        while r0 + dr2 < H and grid[r0 + dr2][s0] != seed:
            dr2 += 1
        period = dr2
        out = [[0]*W for _ in range(H)]
        k = 0
        while True:
            base = r0 + k*period
            if base >= H:
                break
            for d in range(pat_h):
                r = base + d
                if 0 <= r < H:
                    for c in mask:
                        v = pattern[d][c]
                        if v:
                            out[r][c] = v
            k += 1
        return out
    else:
        r0 = None
        for i, row in enumerate(grid):
            segs = []
            c = 0
            while c < W:
                if row[c] != 0:
                    s = c
                    while c < W and row[c] != 0:
                        c += 1
                    if c - s >= 4:
                        segs.append(s)
                else:
                    c += 1
            if len(segs) >= 2:
                r0 = i
                s0 = segs[0]
                break
        if r0 is None:
            return [[0]*W for _ in range(H)]
        dr = 1
        while r0 + dr < H and grid[r0 + dr][s0] != 0:
            dr += 1
        pat_h = dr
        mask = set()
        for d in range(pat_h):
            r = r0 + d
            for c in range(W):
                if grid[r][c] != 0:
                    mask.add(c)
        pattern = [[0]*W for _ in range(pat_h)]
        for d in range(pat_h):
            r = r0 + d
            for c in mask:
                v = grid[r][c]
                if v != 0:
                    pattern[d][c] = v
        seed = grid[r0][s0]
        dr2 = 1
        while r0 + dr2 < H and grid[r0 + dr2][s0] != seed:
            dr2 += 1
        period = dr2
        out = [[0]*W for _ in range(H)]
        k = 0
        while True:
            base = r0 + k*period
            if base >= H:
                break
            for d in range(pat_h):
                r = base + d
                if r < H:
                    for c in mask:
                        v = pattern[d][c]
                        if v:
                            out[r][c] = v
            k += 1
        return out