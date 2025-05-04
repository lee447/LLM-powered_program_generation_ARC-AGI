def solve(grid):
    N = len(grid[0])
    c = grid[0].index(2)
    out = [[0]*N for _ in range(N)]
    for i in range(N):
        if 0 <= c - i < N:
            out[i][c - i] = 2
        if 0 <= c + i < N:
            out[i][c + i] = 2
    for i in range(N):
        for j in range(N):
            if out[i][j] == 2 and i % 2 == 0 and j < c:
                k = 1
                while True:
                    ni, nj = i + k, j + k
                    if ni >= N or nj >= N or out[ni][nj] != 0:
                        break
                    out[ni][nj] = 1
                    k += 1
    return out