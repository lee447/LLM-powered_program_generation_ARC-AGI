def solve(grid):
    H, W = len(grid), len(grid[0])
    used = [[False]*W for _ in range(H)]
    runs = []
    for r in range(H):
        c = 0
        while c < W:
            if grid[r][c] != 0:
                col = grid[r][c]
                start = c
                c2 = c + 1
                while c2 < W and grid[r][c2] == col:
                    c2 += 1
                length = c2 - start
                if length >= 2:
                    runs.append((length, col))
                    for cc in range(start, c2):
                        used[r][cc] = True
                c = c2
            else:
                c += 1
    for c in range(W):
        r = 0
        while r < H:
            if grid[r][c] != 0:
                col = grid[r][c]
                start = r
                r2 = r + 1
                while r2 < H and grid[r2][c] == col:
                    r2 += 1
                length = r2 - start
                if length >= 2:
                    runs.append((length, col))
                    for rr in range(start, r2):
                        used[rr][c] = True
                r = r2
            else:
                r += 1
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 0 and not used[r][c]:
                runs.append((1, grid[r][c]))
    runs.sort(key=lambda x: -x[0])
    N = runs[0][0]
    out = [[0]*N for _ in range(N)]
    layers = len(runs)
    for i in range(layers-1):
        offset = i
        color = runs[i][1]
        for x in range(offset, N-offset):
            out[offset][x] = color
            out[N-offset-1][x] = color
        for y in range(offset, N-offset):
            out[y][offset] = color
            out[y][N-offset-1] = color
    offset = layers-1
    end = N - offset
    color = runs[-1][1]
    for r in range(offset, end):
        for c in range(offset, end):
            out[r][c] = color
    return out