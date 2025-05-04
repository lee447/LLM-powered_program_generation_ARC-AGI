def solve(grid):
    n = len(grid)
    color = 0
    for row in grid:
        for v in row:
            if v:
                color = v
                break
        if color:
            break
    B = [[1 if grid[i][j] == 0 else 0 for j in range(n)] for i in range(n)]
    N = n * n
    out = [[0] * N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if B[i][j]:
                bi, bj = i * n, j * n
                for pi in range(n):
                    for pj in range(n):
                        if B[pi][pj]:
                            out[bi + pi][bj + pj] = color
    return out