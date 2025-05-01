def solve(grid):
    h = len(grid)
    w = len(grid[0])
    colors = set()
    for row in grid:
        for v in row:
            if v:
                colors.add(v)
    if 6 in colors:
        # Task 1
        max_run = 0
        for r in range(h):
            c = 0
            while c < w:
                if grid[r][c] != 0:
                    v = grid[r][c]
                    l = 0
                    while c + l < w and grid[r][c + l] == v:
                        l += 1
                    if l > max_run:
                        max_run = l
                    c += l
                else:
                    c += 1
        stripes_rows = []
        for r in range(h):
            c = 0
            ok = False
            while c < w:
                if grid[r][c] != 0:
                    v = grid[r][c]
                    l = 0
                    while c + l < w and grid[r][c + l] == v:
                        l += 1
                    if l == max_run:
                        ok = True
                        break
                    c += l
                else:
                    c += 1
            if ok:
                stripes_rows.append(r)
        stripes_rows.sort()
        first_sr = stripes_rows[0]
        col_ranges = []
        c = 0
        while c < w:
            if grid[first_sr][c] != 0:
                v = grid[first_sr][c]
                start = c
                while c < w and grid[first_sr][c] == v:
                    c += 1
                if c - start == max_run:
                    col_ranges.append((start, c))
            else:
                c += 1
        stripe_height = 1
        for i in range(1, len(stripes_rows)):
            if stripes_rows[i] == first_sr + stripe_height:
                stripe_height += 1
            else:
                break
        diffs = []
        for i in range(len(stripes_rows) - 1):
            diffs.append(stripes_rows[i + 1] - stripes_rows[i] - stripe_height)
        interior_height = min(diffs) if diffs else 0
        interior_row0 = first_sr + stripe_height
        cnt = {}
        for r in range(interior_row0, interior_row0 + interior_height):
            for c0, c1 in col_ranges:
                for c in range(c0, c1):
                    v = grid[r][c]
                    if v:
                        cnt[v] = cnt.get(v, 0) + 1
        items = sorted(cnt.items(), key=lambda x: -x[1])
        if len(items) >= 2:
            primary, filler = items[0][0], items[1][0]
        elif items:
            primary, filler = items[0][0], 0
        else:
            primary, filler = 0, 0
        out = [[0] * w for _ in range(h)]
        for bs in stripes_rows:
            for c0, c1 in col_ranges:
                for c in range(c0, c1):
                    out[bs][c] = grid[bs][c]
            for ir in range(bs + stripe_height, bs + stripe_height + interior_height):
                for c0, c1 in col_ranges:
                    width = c1 - c0
                    for k in range(width):
                        color = primary if ((k // 2) % 2) == 0 else filler
                        out[ir][c0 + k] = color
        return out
    elif 8 in colors:
        # Task 2
        # detect max constant run for filler
        max_run = 0
        for r in range(h):
            c = 0
            while c < w:
                if grid[r][c] != 0:
                    v = grid[r][c]
                    l = 0
                    while c + l < w and grid[r][c + l] == v:
                        l += 1
                    if l > max_run:
                        max_run = l
                    c += l
                else:
                    c += 1
        filler_rows = []
        for r in range(h):
            c = 0
            while c < w:
                if grid[r][c] != 0:
                    v = grid[r][c]
                    l = 0
                    while c + l < w and grid[r][c + l] == v:
                        l += 1
                    if l == max_run:
                        filler_rows.append(r)
                        break
                    c += l
                else:
                    c += 1
        first_f = filler_rows[0]
        col_ranges = []
        c = 0
        while c < w:
            if grid[first_f][c] != 0:
                v = grid[first_f][c]
                start = c
                while c < w and grid[first_f][c] == v:
                    c += 1
                if c - start == max_run:
                    col_ranges.append((start, c))
            else:
                c += 1
        block_width = col_ranges[0][1] - col_ranges[0][0]
        blocks_count = len(col_ranges)
        threshold = blocks_count * block_width // 2 + 1
        stripe_and_filler = []
        for r in range(h):
            cnt = 0
            for c0, c1 in col_ranges:
                for c in range(c0, c1):
                    if grid[r][c] != 0:
                        cnt += 1
            if cnt >= threshold:
                stripe_and_filler.append(r)
        stripe_and_filler = sorted(stripe_and_filler)
        group_starts = [r for r in stripe_and_filler if r - 1 not in stripe_and_filler]
        first_start = group_starts[0]
        block0 = []
        rr = first_start
        sset = set(stripe_and_filler)
        while rr in sset:
            block0.append(rr)
            rr += 1
        bh = len(block0)
        out = [[0] * w for _ in range(h)]
        for s in group_starts:
            for i, src in enumerate(block0):
                dst = s + i
                for c0, c1 in col_ranges:
                    for c in range(c0, c1):
                        out[dst][c] = grid[src][c]
        return out
    else:
        # Task 3
        # detect stripes by max run length
        max_run = 0
        for r in range(h):
            c = 0
            while c < w:
                if grid[r][c] != 0:
                    v = grid[r][c]
                    l = 0
                    while c + l < w and grid[r][c + l] == v:
                        l += 1
                    if l > max_run:
                        max_run = l
                    c += l
                else:
                    c += 1
        stripes_rows = []
        for r in range(h):
            c = 0
            ok = False
            while c < w:
                if grid[r][c] != 0:
                    v = grid[r][c]
                    l = 0
                    while c + l < w and grid[r][c + l] == v:
                        l += 1
                    if l == max_run:
                        ok = True
                        break
                    c += l
                else:
                    c += 1
            if ok:
                stripes_rows.append(r)
        stripes_rows.sort()
        first_sr = stripes_rows[0]
        col_ranges = []
        c = 0
        while c < w:
            if grid[first_sr][c] != 0:
                v = grid[first_sr][c]
                start = c
                while c < w and grid[first_sr][c] == v:
                    c += 1
                if c - start == max_run:
                    col_ranges.append((start, c))
            else:
                c += 1
        group_starts = [r for r in stripes_rows if r - 1 not in stripes_rows]
        # block0 is consecutive stripes
        block0 = []
        rr = first_sr
        sset = set(stripes_rows)
        while rr in sset:
            block0.append(rr)
            rr += 1
        out = [[0] * w for _ in range(h)]
        for s in group_starts:
            for i, src in enumerate(block0):
                dst = s + i
                for c0, c1 in col_ranges:
                    for c in range(c0, c1):
                        out[dst][c] = grid[src][c]
        return out