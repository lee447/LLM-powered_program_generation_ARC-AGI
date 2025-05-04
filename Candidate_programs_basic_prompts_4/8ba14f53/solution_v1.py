from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    bounds = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 0:
                if v not in bounds:
                    bounds[v] = [r, r, c, c]
                else:
                    b = bounds[v]
                    b[0] = min(b[0], r)
                    b[1] = max(b[1], r)
                    b[2] = min(b[2], c)
                    b[3] = max(b[3], c)
    colors = sorted(bounds.items(), key=lambda x: x[1][2])
    A, bA = colors[0]
    B, bB = colors[1]
    def interior_zero_count(b):
        r0, r1, c0, c1 = b
        cnt = 0
        for rr in range(r0 + 1, r1):
            for cc in range(c0 + 1, c1):
                if grid[rr][cc] == 0:
                    cnt += 1
        return cnt
    cntA = interior_zero_count(bA)
    cntB = interior_zero_count(bB)
    out = [[0]*3 for _ in range(3)]
    for i in range(cntA):
        r, c = divmod(i, 3)
        if r < 2:
            out[r][c] = A
    startB = 1 if cntA <= 3 else 2
    for i in range(cntB):
        r = startB + i // 3
        c = i % 3
        if r < 3:
            out[r][c] = B
    return out