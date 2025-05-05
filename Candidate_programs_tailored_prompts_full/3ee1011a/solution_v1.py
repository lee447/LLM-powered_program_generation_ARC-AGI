def solve(grid):
    H = len(grid)
    W = len(grid[0])
    used = [[False]*W for _ in range(H)]
    segs = []
    for i in range(H):
        for j in range(W):
            c = grid[i][j]
            if c != 0 and not used[i][j]:
                horiz = (j+1 < W and grid[i][j+1] == c) or (j-1 >= 0 and grid[i][j-1] == c)
                vert = (i+1 < H and grid[i+1][j] == c) or (i-1 >= 0 and grid[i-1][j] == c)
                if horiz:
                    jj = j
                    while jj-1 >= 0 and grid[i][jj-1] == c:
                        jj -= 1
                    length = 0
                    coords = []
                    while jj < W and grid[i][jj] == c:
                        coords.append((i, jj))
                        length += 1
                        jj += 1
                    for x,y in coords:
                        used[x][y] = True
                    segs.append((length, c))
                elif vert:
                    ii = i
                    while ii-1 >= 0 and grid[ii-1][j] == c:
                        ii -= 1
                    length = 0
                    coords = []
                    while ii < H and grid[ii][j] == c:
                        coords.append((ii, j))
                        length += 1
                        ii += 1
                    for x,y in coords:
                        used[x][y] = True
                    segs.append((length, c))
                else:
                    used[i][j] = True
                    segs.append((1, c))
    segs.sort(key=lambda x: -x[0])
    N = segs[0][0]
    res = [[0]*N for _ in range(N)]
    for idx, (length, color) in enumerate(segs):
        offset = idx
        size = N - 2*idx
        if size <= 0:
            break
        s = offset
        e = offset + size - 1
        if size <= 2:
            for x in range(s, s+size):
                for y in range(s, s+size):
                    res[x][y] = color
        else:
            for y in range(s, e+1):
                res[s][y] = color
                res[e][y] = color
            for x in range(s, e+1):
                res[x][s] = color
                res[x][e] = color
    return res