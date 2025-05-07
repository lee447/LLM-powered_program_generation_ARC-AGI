from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    hmatch = sum(grid[i][j] == grid[H-1-i][j] for i in range(H) for j in range(W))
    vmatch = sum(grid[i][j] == grid[i][W-1-j] for i in range(H) for j in range(W))
    horiz = hmatch > vmatch
    r0, r1, c0, c1 = H, -1, W, -1
    for i in range(H):
        for j in range(W):
            if horiz:
                if grid[i][j] != grid[H-1-i][j]:
                    r0 = min(r0, i, H-1-i); r1 = max(r1, i, H-1-i)
                    c0 = min(c0, j); c1 = max(c1, j)
            else:
                if grid[i][j] != grid[i][W-1-j]:
                    r0 = min(r0, i); r1 = max(r1, i)
                    c0 = min(c0, j, W-1-j); c1 = max(c1, j, W-1-j)
    orig = [row[:] for row in grid]
    for i in range(r0, r1+1):
        for j in range(c0, c1+1):
            if horiz:
                grid[i][j] = orig[H-1-i][j]
            else:
                grid[i][j] = orig[i][W-1-j]
    return [row[c0:c1+1] for row in grid[r0:r1+1]]