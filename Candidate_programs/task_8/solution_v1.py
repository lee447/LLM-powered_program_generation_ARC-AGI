def solve(grid):
    n = len(grid)
    m = len(grid[0])
    sep_rows = [i for i in range(n) if all(v==0 for v in grid[i])]
    sep_cols = [j for j in range(m) if all(grid[i][j]==0 for i in range(n))]
    row_ints = [(sep_rows[i]+1, sep_rows[i+1]-1) for i in range(len(sep_rows)-1) if sep_rows[i+1]-sep_rows[i]>1]
    col_ints = [(sep_cols[i]+1, sep_cols[i+1]-1) for i in range(len(sep_cols)-1) if sep_cols[i+1]-sep_cols[i]>1]
    B = len(row_ints)
    blocks = [[None]*B for _ in range(B)]
    for bi,(r0,r1) in enumerate(row_ints):
        for bj,(c0,c1) in enumerate(col_ints):
            blocks[bi][bj] = [grid[i][c0:c1+1] for i in range(r0,r1+1)]
    def mode(L):
        d={}
        for x in L:
            d[x]=d.get(x,0)+1
        return max(d,key=d.get)
    mask_map = {
        (1,0,0,0):(0,0),(1,1,0,0):(0,1),(0,1,0,0):(0,2),
        (1,0,0,1):(1,0),(1,1,1,1):(1,1),(0,1,1,0):(1,2),
        (0,0,0,1):(2,0),(0,0,1,1):(2,1),(0,0,1,0):(2,2)
    }
    out_blocks = [[None]*B for _ in range(B)]
    for bi in range(B):
        for bj in range(B):
            blk = blocks[bi][bj]
            flat = [c for row in blk for c in row]
            bg = mode([v for v in flat if v!=0])
            s = len(blk)
            mid = s//2
            corners = []
            for xs in [(0,1),(0,1),(mid,mid+1),(mid,mid+1)]:
                pass
            c0 = any(blk[i][j]!=bg for i in (0,1) for j in (0,1))
            c1 = any(blk[i][j]!=bg for i in (0,1) for j in (s-2,s-1))
            c2 = any(blk[i][j]!=bg for i in (s-2,s-1) for j in (s-2,s-1))
            c3 = any(blk[i][j]!=bg for i in (s-2,s-1) for j in (0,1))
            key = (1 if c0 else 0,1 if c1 else 0,1 if c2 else 0,1 if c3 else 0)
            ti,tj = mask_map[key]
            out_blocks[ti][tj] = blk
    out = [[0]*m for _ in range(n)]
    for bi,(r0,r1) in enumerate(row_ints):
        for bj,(c0,c1) in enumerate(col_ints):
            blk = out_blocks[bi][bj]
            for i in range(r0,r1+1):
                for j in range(c0,c1+1):
                    out[i][j] = blk[i-r0][j-c0]
    return out