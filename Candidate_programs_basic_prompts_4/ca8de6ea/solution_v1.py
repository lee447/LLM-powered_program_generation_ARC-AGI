from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    m = len(grid)
    mid = (m - 1) // 2
    n = mid + 1
    diag1 = [grid[i][i] for i in range(m)]
    diag2 = [grid[i][m - 1 - i] for i in range(m)]
    out = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0:
                if j < mid:
                    out[i][j] = diag1[j]
                else:
                    out[i][j] = diag2[0]
            elif i < mid:
                if j == 0:
                    out[i][j] = diag2[i]
                elif j == i:
                    out[i][j] = diag1[mid]
                else:
                    out[i][j] = diag2[mid + i]
            else:
                if j == 0:
                    out[i][j] = diag2[m - 1]
                else:
                    out[i][j] = diag1[mid + j]
    return out