from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bw = w // 3
    out = [[0]*w for _ in range(h)]
    for i in range(3):
        c0 = i * bw
        A = [[grid[r][c0 + j] == 5 for j in range(bw)] for r in range(h)]
        total = sum(sum(row) for row in A)
        if total == 1 and A[1][1]:
            col = 4
        elif total == bw and all(A[0][j] for j in range(bw)):
            col = 6
        elif total == bw and all(A[h-1][j] for j in range(bw)):
            col = 1
        elif total == 3 and A[0][bw-1] and A[1][1] and A[2][0]:
            col = 9
        elif total == h*bw - 1 and not A[1][1]:
            col = 3
        else:
            col = 0
        for r in range(h):
            for j in range(bw):
                out[r][c0 + j] = col
    return out