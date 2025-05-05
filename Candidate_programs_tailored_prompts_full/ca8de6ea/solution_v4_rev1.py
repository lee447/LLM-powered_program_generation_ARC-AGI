from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    if n == 0: return []
    mid = n // 2
    m = mid + 1
    c = m // 2
    main = [grid[i][i] for i in range(n)]
    anti = [grid[i][n - 1 - i] for i in range(n)]
    s = mid - (m - 1) // 2
    e = s + m - 1
    out = [[0] * m for _ in range(m)]
    for k in range(m):
        out[k][c] = main[s + k]
        out[c][k] = anti[s + k]
    out[0][0] = main[s - 1]
    out[0][m - 1] = anti[s - 1]
    out[m - 1][0] = anti[e + 1]
    out[m - 1][m - 1] = main[e + 1]
    return out