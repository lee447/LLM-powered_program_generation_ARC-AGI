from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    d1 = [grid[i][i] for i in range(n)]
    d2 = [grid[i][n-1-i] for i in range(n)]
    k = n - 2
    mid = n // 2
    r = [[0] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            if i == 0:
                if j < k - 1:
                    r[i][j] = d1[j]
                else:
                    r[i][j] = d2[0]
            elif i == k - 1:
                if j > 0:
                    r[i][j] = d1[n - k + j]
                else:
                    r[i][j] = d2[n - 1]
            else:
                if j == 0:
                    r[i][j] = d2[i]
                elif j == k - 1:
                    r[i][j] = d2[n - 1 - i]
                else:
                    r[i][j] = d1[mid]
    return r