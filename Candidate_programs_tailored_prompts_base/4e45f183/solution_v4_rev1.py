from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    zero_rows = [i for i in range(H) if all(x == 0 for x in grid[i])]
    zero_cols = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    block_h = zero_rows[1] - zero_rows[0] - 1
    block_w = zero_cols[1] - zero_cols[0] - 1
    blockRowStarts = [zero_rows[i] + 1 for i in range(len(zero_rows) - 1)]
    blockColStarts = [zero_cols[j] + 1 for j in range(len(zero_cols) - 1)]
    B_h, B_w = len(blockRowStarts), len(blockColStarts)
    # find target color
    from collections import Counter
    cnt = Counter()
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 0:
                cnt[v] += 1
    C, _ = min((col, cnt[col]) for col in cnt)
    # map rows/cols to block indices
    row2b = [None]*H
    for bi, r0 in enumerate(blockRowStarts):
        for dr in range(block_h):
            row2b[r0+dr] = bi
    col2b = [None]*W
    for bj, c0 in enumerate(blockColStarts):
        for dc in range(block_w):
            col2b[c0+dc] = bj
    # collect all C positions
    brs = set()
    bcs = set()
    for r in range(H):
        for c in range(W):
            if grid[r][c] == C and row2b[r] is not None and col2b[c] is not None:
                brs.add(row2b[r])
                bcs.add(col2b[c])
    if not brs or not bcs:
        return grid
    minbr, maxbr = min(brs), max(brs)
    minbc, maxbc = min(bcs), max(bcs)
    l = maxbr - minbr + 1
    k = maxbc - minbc + 1
    PH = l*block_h
    PW = k*block_w
    # extract pattern mask
    pat = [[False]*PW for _ in range(PH)]
    for r in range(H):
        bi = row2b[r]
        if bi is None or not (minbr <= bi <= maxbr): continue
        for c in range(W):
            bj = col2b[c]
            if bj is None or not (minbc <= bj <= maxbc): continue
            if grid[r][c] == C:
                pr = (bi - minbr)*block_h + (r - blockRowStarts[bi])
                pc = (bj - minbc)*block_w + (c - blockColStarts[bj])
                pat[pr][pc] = True
    # slide over all valid offsets
    for dbr in range(-minbr, B_h - maxbr):
        for dbc in range(-minbc, B_w - maxbc):
            for pr in range(PH):
                br0 = minbr + pr//block_h + dbr
                if br0 < 0 or br0 >= B_h: continue
                inner_r = pr % block_h
                for pc in range(PW):
                    if not pat[pr][pc]: continue
                    bc0 = minbc + pc//block_w + dbc
                    if bc0 < 0 or bc0 >= B_w: continue
                    inner_c = pc % block_w
                    rr = blockRowStarts[br0] + inner_r
                    cc = blockColStarts[bc0] + inner_c
                    grid[rr][cc] = C
    return grid