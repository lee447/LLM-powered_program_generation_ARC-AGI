from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    cells = [(i, j) for i in range(H) for j in range(W) if grid[i][j] != 0]
    r0 = min(i for i, _ in cells)
    c0 = min(j for _, j in cells)
    s = 0
    while c0 + s < W and grid[r0][c0 + s] != 0:
        s += 1
    grid0 = [grid[r0 + i][c0:c0 + s] for i in range(s)]
    block_H = [row[::-1] for row in grid0]
    block_V = grid0[::-1]
    block_R = [row[::-1] for row in grid0[::-1]]
    mTR, mBL, mBR = {}, {}, {}
    for i in range(s):
        for j in range(s):
            v = grid[r0 + i][c0 + s + j]
            if v:
                mTR[block_H[i][j]] = v
            v = grid[r0 + s + i][c0 + j]
            if v:
                mBL[block_V[i][j]] = v
            v = grid[r0 + s + i][c0 + s + j]
            if v:
                mBR[block_R[i][j]] = v
    out = [[0] * W for _ in range(H)]
    for i in range(s):
        for j in range(s):
            out[r0 + i][c0 + j] = grid0[i][j]
            out[r0 + i][c0 + s + j] = mTR.get(block_H[i][j], 0)
            out[r0 + s + i][c0 + j] = mBL.get(block_V[i][j], 0)
            out[r0 + s + i][c0 + s + j] = mBR.get(block_R[i][j], 0)
    return out