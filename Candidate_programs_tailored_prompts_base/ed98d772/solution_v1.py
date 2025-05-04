def solve(grid):
    n = len(grid)
    N = 2 * n
    for h in range(n):
        for v in range(n):
            out = [[None] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    bi, bj = i // n, j // n
                    li, lj = i % n, j % n
                    si = (li - bi * v) % n
                    sj = (lj - bj * h) % n
                    out[i][j] = grid[si][sj]
            cols = []
            for c in range(N):
                if all(out[i][c] == 0 for i in range(N)):
                    cols.append(c)
            if len(cols) == 1:
                return out
    return []