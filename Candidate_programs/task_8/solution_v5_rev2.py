def solve(grid):
    from collections import Counter
    n, m = len(grid), len(grid[0])
    sep_rows = [i for i in range(n) if all(v == 0 for v in grid[i])]
    sep_cols = [j for j in range(m) if all(grid[i][j] == 0 for i in range(n))]
    row_ints = [(sep_rows[i] + 1, sep_rows[i + 1] - 1) for i in range(len(sep_rows) - 1)]
    col_ints = [(sep_cols[i] + 1, sep_cols[i + 1] - 1) for i in range(len(sep_cols) - 1)]
    B = len(row_ints)
    blocks = []
    for bi, (r0, r1) in enumerate(row_ints):
        for bj, (c0, c1) in enumerate(col_ints):
            blk = [grid[i][c0:c1+1] for i in range(r0, r1+1)]
            blocks.append((bi, bj, blk))
    def mode_nonzero(lst):
        cnt = Counter(v for v in lst if v)
        return cnt and cnt.most_common(1)[0][0] or 0
    mask_map = {
        (1,0,0,0):(0,0),(1,1,0,0):(0,1),(0,1,0,0):(0,2),
        (1,0,0,1):(1,0),(1,1,1,1):(1,1),(0,1,1,0):(1,2),
        (0,0,0,1):(2,0),(0,0,1,1):(2,1),(0,0,1,0):(2,2)
    }
    out_blocks = [[None]*B for _ in range(B)]
    used = set()
    for bi, bj, blk in blocks:
        flat = [c for row in blk for c in row]
        bg = mode_nonzero(flat)
        s = len(blk)
        c0 = any(blk[i][j] != bg for i in (0,1) for j in (0,1))
        c1 = any(blk[i][j] != bg for i in (0,1) for j in (s-2,s-1))
        c2 = any(blk[i][j] != bg for i in (s-2,s-1) for j in (s-2,s-1))
        c3 = any(blk[i][j] != bg for i in (s-2,s-1) for j in (0,1))
        pos = mask_map.get((c0,c1,c2,c3),(bi,bj))
        ti, tj = pos
        if out_blocks[ti][tj] is None:
            out_blocks[ti][tj] = blk
            used.add((bi,bj))
    leftovers = [blk for bi,bj,blk in blocks if (bi,bj) not in used]
    it = iter(leftovers)
    for i in range(B):
        for j in range(B):
            if out_blocks[i][j] is None:
                out_blocks[i][j] = next(it)
    out = [[0]*m for _ in range(n)]
    for ti, (r0, r1) in enumerate(row_ints):
        for tj, (c0, c1) in enumerate(col_ints):
            blk = out_blocks[ti][tj]
            for i in range(r0, r1+1):
                for j in range(c0, c1+1):
                    out[i][j] = blk[i-r0][j-c0]
    return out