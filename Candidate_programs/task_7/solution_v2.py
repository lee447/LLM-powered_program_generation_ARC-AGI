def solve(grid):
    H, W = len(grid), len(grid[0])
    sep = 4
    rows = [i for i in range(H) if sum(1 for x in grid[i] if x == sep) > W*2//3]
    cols = [j for j in range(W) if sum(1 for i in range(H) if grid[i][j] == sep) > H*2//3]
    rcuts = [-1] + rows + [H]
    ccuts = [-1] + cols + [W]
    blocks = []
    for bi in range(len(rcuts)-1):
        r0, r1 = rcuts[bi]+1, rcuts[bi+1]-1
        if r0>r1: continue
        row_blocks = []
        for bj in range(len(ccuts)-1):
            c0, c1 = ccuts[bj]+1, ccuts[bj+1]-1
            if c0>c1: continue
            sub = [row[c0:c1+1] for row in grid[r0:r1+1]]
            row_blocks.append((r0,c0,sub))
        blocks.append(row_blocks)
    # find big block
    bi0 = bj0 = None
    for i, rb in enumerate(blocks):
        for j, (_,_,sub) in enumerate(rb):
            if len(sub) > 3 and len(sub[0]) > 3:
                bi0, bj0 = i, j
    r0, c0, big = blocks[bi0][bj0]
    B, Bc = len(big), len(big[0])
    arr = [row[1: Bc-1] for row in big[1: B-1]]
    out = [list(row) for row in grid]
    Rb = len(blocks)
    Cb = len(blocks[0])
    for i in range(Rb):
        for j in range(Cb):
            if i==bi0 and j==bj0: continue
            r0, c0, sub = blocks[i][j]
            if len(sub)!=3 or len(sub[0])!=3: continue
            if i < bi0:
                rr = i
            else:
                rr = i - (1 if i>bi0 else 0)
            if j < bj0:
                cc = j
            else:
                cc = j - (1 if j>bj0 else 0)
            if rr<0 or rr>=len(arr) or cc<0 or cc>=len(arr[0]): continue
            color = arr[rr][cc]
            if color == 0: continue
            for di in range(3):
                for dj in range(3):
                    if grid[r0+di][c0+dj] == 1:
                        out[r0+di][c0+dj] = color
    return out