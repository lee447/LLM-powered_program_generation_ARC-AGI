from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    r0, r1, c0, c1 = H, -1, W, -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 0:
                if i < r0: r0 = i
                if i > r1: r1 = i
                if j < c0: c0 = j
                if j > c1: c1 = j
    cntH = totH = 0
    for i in range(H):
        j2 = H - 1 - i
        if i < j2:
            for j in range(W):
                a, b = grid[i][j], grid[j2][j]
                if a and b:
                    totH += 1
                    if a == b: cntH += 1
    cntV = totV = 0
    for j in range(W):
        k2 = W - 1 - j
        if j < k2:
            for i in range(H):
                a, b = grid[i][j], grid[i][k2]
                if a and b:
                    totV += 1
                    if a == b: cntV += 1
    horiz = cntH * (totV or 1) > cntV * (totH or 1)
    for i in range(r0, r1+1):
        for j in range(c0, c1+1):
            if horiz:
                grid[i][j] = grid[H-1-i][j]
            else:
                grid[i][j] = grid[i][W-1-j]
    return [row[c0:c1+1] for row in grid[r0:r1+1]]