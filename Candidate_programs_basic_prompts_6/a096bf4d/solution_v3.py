def solve(grid):
    H, W = len(grid), len(grid[0])
    row_sep = [i for i in range(H) if all(x == 0 for x in grid[i])]
    col_sep = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    row_blocks = [(row_sep[i] + 1, row_sep[i+1]) for i in range(len(row_sep)-1)]
    col_blocks = [(col_sep[j] + 1, col_sep[j+1]) for j in range(len(col_sep)-1)]
    br0_start, br0_end = row_blocks[0]
    bc0_start, bc0_end = col_blocks[0]
    bh, bw = br0_end - br0_start, bc0_end - bc0_start
    template = [row[bc0_start:bc0_end] for row in grid[br0_start:br0_end]]
    from collections import Counter
    cnt = Counter()
    for r in template:
        cnt.update(r)
    bg = cnt.most_common(1)[0][0]
    tpos = [(i,j) for i in range(bh) for j in range(bw) if template[i][j] != bg]
    tpos.sort()
    out = [row[:] for row in grid]
    for bi, (rs, re) in enumerate(row_blocks):
        for bj, (cs, ce) in enumerate(col_blocks):
            if bi==0 and bj==0: continue
            block = [row[cs:ce] for row in grid[rs:re]]
            cntb = Counter()
            for r in block:
                cntb.update(r)
            uc = next(k for k,v in cntb.items() if k!=bg and v==1)
            for i in range(bh):
                for j in range(bw):
                    out[rs+i][cs+j] = bg
            for idx, (i,j) in enumerate(tpos):
                if idx==0:
                    out[rs+i][cs+j] = uc
                else:
                    out[rs+i][cs+j] = template[i][j]
    return out