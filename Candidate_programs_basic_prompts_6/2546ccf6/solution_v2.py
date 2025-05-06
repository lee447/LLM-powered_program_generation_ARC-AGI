from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0])
    bg = 0
    stripeRows = [i for i in range(H) if grid[i][0] != bg and all(grid[i][j] == grid[i][0] for j in range(W))]
    stripeCols = [j for j in range(W) if grid[0][j] != bg and all(grid[i][j] == grid[0][j] for i in range(H))]
    stripeRows.sort()
    stripeCols.sort()
    stripeColor = grid[stripeRows[0]][0] if stripeRows else None
    rowBounds = [-1] + stripeRows + [H]
    colBounds = [-1] + stripeCols + [W]
    rowBlocks = [(rowBounds[i]+1, rowBounds[i+1]-1) for i in range(len(rowBounds)-1) if rowBounds[i]+1 <= rowBounds[i+1]-1]
    colBlocks = [(colBounds[i]+1, colBounds[i+1]-1) for i in range(len(colBounds)-1) if colBounds[i]+1 <= colBounds[i+1]-1]
    rowBlockOf = [-1]*H
    for b,(rs, re) in enumerate(rowBlocks):
        for i in range(rs, re+1):
            rowBlockOf[i] = b
    colBlockOf = [-1]*W
    for b,(cs, ce) in enumerate(colBlocks):
        for j in range(cs, ce+1):
            colBlockOf[j] = b
    out = [row[:] for row in grid]
    nb = len(colBlocks)
    for k in range(1, len(colBlocks)-1):
        left_b = k
        right_b = k+1
        cs_l, ce_l = colBlocks[left_b]
        cs_r, ce_r = colBlocks[right_b]
        w_l = ce_l - cs_l + 1
        w_r = ce_r - cs_r + 1
        if w_l != w_r: continue
        for (rs, re) in rowBlocks:
            # collect blocks used
            used = set()
            for i in range(rs, re+1):
                for j in range(W):
                    v = grid[i][j]
                    if v != bg and v != stripeColor:
                        b = colBlockOf[j]
                        if b != -1:
                            used.add(b)
            if not used or not used.issubset({left_b, right_b}):
                continue
            posL = [(i,j) for i in range(rs, re+1) for j in range(cs_l, ce_l+1) if grid[i][j] != bg and grid[i][j] != stripeColor]
            posR = [(i,j) for i in range(rs, re+1) for j in range(cs_r, ce_r+1) if grid[i][j] != bg and grid[i][j] != stripeColor]
            if posL and not posR:
                for i,j in posL:
                    d = j - cs_l
                    j2 = cs_r + (w_l-1-d)
                    out[i][j2] = grid[i][j]
            elif posR and not posL:
                for i,j in posR:
                    d = j - cs_r
                    j2 = cs_l + (w_l-1-d)
                    out[i][j2] = grid[i][j]
    return out