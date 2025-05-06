def solve(grid):
    R = len(grid)
    C = len(grid[0])
    zero_rows = [i for i in range(R) if all(v==0 for v in grid[i])]
    zero_cols = [j for j in range(C) if all(grid[i][j]==0 for i in range(R))]
    rsegs = []
    prev = -1
    for zr in zero_rows:
        if zr - prev > 1:
            rsegs.append((prev+1, zr))
        prev = zr
    prev = -1
    csegs = []
    for zc in zero_cols:
        if zc - prev > 1:
            csegs.append((prev+1, zc))
        prev = zc
    blocks = []
    for rs, re in rsegs:
        for cs, ce in csegs:
            blk = [row[cs:ce] for row in grid[rs:re]]
            blocks.append(blk)
    mapping = [1,0,4,1,0,4,2,5,8]
    newblks = [blocks[m] for m in mapping]
    out = [[0]*C for _ in range(R)]
    bi = 0
    for (rs,re) in rsegs:
        for (cs,ce) in csegs:
            blk = newblks[bi]
            for i in range(re-rs):
                out[rs+i][cs:cs+ce-cs] = blk[i]
            bi += 1
    return out