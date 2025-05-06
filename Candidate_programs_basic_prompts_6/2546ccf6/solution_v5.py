def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_rows = [r for r in range(h) if grid[r][0] != 0 and all(grid[r][c] == grid[r][0] for c in range(w))]
    sep_cols = [c for c in range(w) if grid[0][c] != 0 and all(grid[r][c] == grid[0][c] for r in range(h))]
    sep_color = grid[sep_rows[0]][0] if sep_rows else None
    def make_ranges(seps, limit):
        if not seps:
            return [(0, limit - 1)]
        seps = sorted(seps)
        rs = []
        if seps[0] > 0:
            rs.append((0, seps[0] - 1))
        for i in range(len(seps) - 1):
            a, b = seps[i], seps[i+1]
            if b - a > 1:
                rs.append((a+1, b-1))
        if seps[-1] < limit - 1:
            rs.append((seps[-1] + 1, limit - 1))
        return rs
    row_stripes = make_ranges(sep_rows, h)
    col_blocks = make_ranges(sep_cols, w)
    counts = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0 and v != sep_color:
                counts[v] = counts.get(v, 0) + 1
    if not counts:
        return grid
    target = max(counts, key=lambda x: counts[x])
    out = [row[:] for row in grid]
    for rs, re in row_stripes:
        # find blocks in this stripe containing target
        bs = []
        for bi, (cs, ce) in enumerate(col_blocks):
            found = False
            for r in range(rs, re+1):
                for c in range(cs, ce+1):
                    if grid[r][c] == target:
                        found = True
                        break
                if found:
                    break
            if found:
                bs.append(bi)
        if len(bs)==1:
            j = bs[0]
            nj = j+1
            if nj < len(col_blocks):
                # check target not in next block
                cs2, ce2 = col_blocks[nj]
                has2 = any(grid[r][c]==target for r in range(rs,re+1) for c in range(cs2,ce2+1))
                if not has2:
                    cs1, ce1 = col_blocks[j]
                    shift = cs2 - cs1
                    for r in range(rs, re+1):
                        for c in range(cs1, ce1+1):
                            if grid[r][c] == target:
                                out[r][c+shift] = target
    return out