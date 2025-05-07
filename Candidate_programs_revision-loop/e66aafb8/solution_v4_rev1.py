from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    totH = cntH = totV = cntV = 0
    for i in range(H):
        hi = H - 1 - i
        if i < hi:
            for j in range(W):
                a, b = grid[i][j], grid[hi][j]
                if a != 0 or b != 0:
                    totH += 1
                    if a == b:
                        cntH += 1
    for j in range(W):
        wj = W - 1 - j
        if j < wj:
            for i in range(H):
                a, b = grid[i][j], grid[i][wj]
                if a != 0 or b != 0:
                    totV += 1
                    if a == b:
                        cntV += 1
    horiz = cntH * (totV or 1) > cntV * (totH or 1)
    zr0 = H; zr1 = -1; zc0 = W; zc1 = -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 0:
                zr0 = min(zr0, i); zr1 = max(zr1, i)
                zc0 = min(zc0, j); zc1 = max(zc1, j)
    if zr1 != -1:
        r0, r1, c0, c1 = zr0, zr1, zc0, zc1
        if horiz:
            c0 = max(0, c0 - 1)
        else:
            r0 = max(0, r0 - 1)
    else:
        r0 = H; r1 = -1; c0 = W; c1 = -1
        for i in range(H):
            for j in range(W):
                if horiz:
                    if grid[i][j] != grid[H-1-i][j]:
                        r0 = min(r0, i); r1 = max(r1, i)
                        c0 = min(c0, j); c1 = max(c1, j)
                else:
                    if grid[i][j] != grid[i][W-1-j]:
                        r0 = min(r0, i); r1 = max(r1, i)
                        c0 = min(c0, j); c1 = max(c1, j)
    if r1 < r0 or c1 < c0:
        return []
    for i in range(r0, r1+1):
        for j in range(c0, c1+1):
            if horiz:
                grid[i][j] = grid[H-1-i][j]
            else:
                grid[i][j] = grid[i][W-1-j]
    return [row[c0:c1+1] for row in grid[r0:r1+1]]