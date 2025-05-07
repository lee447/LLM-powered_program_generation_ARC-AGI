from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    N = len(grid)
    m = [grid[i][i] for i in range(N)]
    a = [grid[i][N-1-i] for i in range(N)]
    K = (N + 1) // 2
    out = [[0] * K for _ in range(K)]
    for i in range(K):
        for j in range(K):
            if i == j:
                out[i][j] = m[2*i]
            elif i + j == K - 1:
                out[i][j] = a[2*i]
            elif i + j < K - 1:
                if j > i:
                    out[i][j] = m[j]
                else:
                    out[i][j] = a[i]
            else:
                if j > i:
                    out[i][j] = a[i]
                else:
                    out[i][j] = m[j]
    return out