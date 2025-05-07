import sys
def solve(grid):
    m, n = len(grid), len(grid[0])
    zeros = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 0}
    best = []
    for dr, dc in ((1, 1), (1, -1)):
        for i, j in zeros:
            pi, pj = i - dr, j - dc
            if 0 <= pi < m and 0 <= pj < n and (pi, pj) in zeros:
                continue
            ni, nj = i + dr, j + dc
            if not (0 <= ni < m and 0 <= nj < n and (ni, nj) in zeros):
                continue
            chain = []
            x, y = i, j
            while (x, y) in zeros:
                chain.append((x, y))
                x, y = x + dr, y + dc
            if len(chain) > len(best):
                best = chain
    out = [row[:] for row in grid]
    for i, j in best:
        out[i][j] = 8
    return out