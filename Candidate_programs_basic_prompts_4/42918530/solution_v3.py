from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    B = (H - 1) // 6
    C = (W - 1) // 6
    br = [1 + i * 6 for i in range(B)]
    bc = [1 + j * 6 for j in range(C)]
    templates = {}
    r0 = br[0]
    for c0 in bc:
        col = grid[r0][c0]
        if col and col not in templates:
            cnt = 0
            for di in range(1, 4):
                for dj in range(1, 4):
                    if grid[r0 + di][c0 + dj] != 0:
                        cnt += 1
            if cnt > 0:
                pat = [[grid[r0 + di][c0 + dj] for dj in range(1, 4)] for di in range(1, 4)]
                templates[col] = pat
    out = [row[:] for row in grid]
    for r0 in br:
        for c0 in bc:
            col = grid[r0][c0]
            if col in templates:
                pat = templates[col]
                for di in range(3):
                    for dj in range(3):
                        out[r0 + 1 + di][c0 + 1 + dj] = pat[di][dj]
    return out