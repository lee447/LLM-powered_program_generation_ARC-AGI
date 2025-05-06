def solve(grid):
    h = len(grid)
    w = len(grid[0])
    zero_rows = [all(c == 0 for c in row) for row in grid]
    zero_cols = [all(grid[r][c] == 0 for r in range(h)) for c in range(w)]
    row_blocks = []
    i = 0
    while i < h:
        if not zero_rows[i]:
            j = i
            while j < h and not zero_rows[j]:
                j += 1
            row_blocks.append((i, j - 1))
            i = j
        else:
            i += 1
    col_blocks = []
    j = 0
    while j < w:
        if not zero_cols[j]:
            k = j
            while k < w and not zero_cols[k]:
                k += 1
            col_blocks.append((j, k - 1))
            j = k
        else:
            j += 1
    # find blocks
    blocks = []
    for r0, r1 in row_blocks:
        for c0, c1 in col_blocks:
            color = grid[r0][c0 + 1]
            if color != 0:
                blocks.append((color, r0, r1, c0, c1))
    # group by color
    from collections import defaultdict
    groups = defaultdict(list)
    for color, r0, r1, c0, c1 in blocks:
        groups[color].append((r0, r1, c0, c1))
    # detect plus reference
    refs = {}
    for color, blks in groups.items():
        best = None
        bestcnt = 0
        for r0, r1, c0, c1 in blks:
            cnt = 0
            for dr, dc in [(1, c0 + (c1 - c0) // 2), (r0 + (r1 - r0) // 2, c0 + 1), (r0 + (r1 - r0) // 2, c0 + (c1 - c0) // 2), (r0 + (r1 - r0) // 2, c1 - 1), (r1 - 1, c0 + (c1 - c0) // 2)]:
                if grid[dr][dc] == color:
                    cnt += 1
            if cnt > bestcnt:
                bestcnt = cnt
                best = (r0, r1, c0, c1)
        if bestcnt == 5:
            refs[color] = best
    # apply
    out = [row[:] for row in grid]
    for color, ref in refs.items():
        for (c, r0, r1, c0, c1) in []: pass
    for color, blks in groups.items():
        if color in refs:
            for r0, r1, c0, c1 in blks:
                # leave reference unchanged
                if (r0, r1, c0, c1) == refs[color]:
                    continue
                midr = r0 + (r1 - r0) // 2
                midc = c0 + (c1 - c0) // 2
                out[r0 + 1][midc] = color
                out[midr][c0 + 1] = color
                out[midr][midc] = color
                out[midr][c1 - 1] = color
                out[r1 - 1][midc] = color
    return out