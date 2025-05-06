from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    row = grid[0]
    n = len(row)
    mid = n // 2
    out = [[0] * n for _ in range(n)]
    red = row[mid]
    for i in range(mid + 1):
        out[i][mid - i] = red
        out[i][mid + i] = red
    maxk = (mid + n - 1) // 4
    start0 = (mid + 1) // 2
    for k in range(1, maxk + 1):
        d = mid - 4 * k
        r0 = start0 + 2 * (k - 1)
        for r in range(r0, n):
            c = r + d
            if 0 <= c < n and out[r][c] == 0:
                out[r][c] = 1
    return out