from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    # find the two non‐zero colors
    colors = sorted({grid[r][c] for r in range(H) for c in range(W) if grid[r][c] != 0})
    # compute bounding box for each color
    def bbox(val):
        rows = [r for r in range(H) for c in range(W) if grid[r][c] == val]
        cols = [c for r in range(H) for c in range(W) if grid[r][c] == val]
        return min(rows), max(rows), min(cols), max(cols)
    b0 = bbox(colors[0])
    b1 = bbox(colors[1])
    # decide left vs right by column
    if b0[2] < b1[2]:
        r1L, r2L, c1L, c2L = b0
        r1R, r2R, c1R, c2R = b1
    else:
        r1L, r2L, c1L, c2L = b1
        r1R, r2R, c1R, c2R = b0
    # crop blocks
    blockL = [grid[r][c1L:c2L+1] for r in range(r1L, r2L+1)]
    blockR = [grid[r][c1R:c2R+1] for r in range(r1R, r2R+1)]
    # trim to leftmost 3 columns
    blockL = [row[:3] + [0]*(3 - len(row[:3])) for row in blockL]
    blockR = [row[:3] + [0]*(3 - len(row[:3])) for row in blockR]
    # pick the left block strip (middle row)
    hL = len(blockL)
    iL = hL // 2
    stripL = blockL[iL]
    # pick the right block strip (middle or lower)
    hR = len(blockR)
    if hR == 3:
        iR = 1
    else:
        iR = 2
    stripR = blockR[iR]
    # assemble output
    out = []
    out.append(stripL[:3])
    out.append(stripR[:3])
    out.append([0,0,0])
    return out