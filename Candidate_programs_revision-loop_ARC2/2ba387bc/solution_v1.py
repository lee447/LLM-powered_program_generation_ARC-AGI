def solve(grid):
    r = len(grid)
    c = len(grid[0])
    hollow = []
    filled = []
    for i in range(r - 3):
        for j in range(c - 3):
            col = grid[i][j]
            if col == 0:
                continue
            ok = True
            for di in range(4):
                for dj in range(4):
                    if di in (0, 3) or dj in (0, 3):
                        if grid[i+di][j+dj] != col:
                            ok = False
                            break
                if not ok:
                    break
            if not ok:
                continue
            is_hollow = False
            for di in (1, 2):
                for dj in (1, 2):
                    if grid[i+di][j+dj] != col:
                        is_hollow = True
                        break
                if is_hollow:
                    break
            if is_hollow:
                hollow.append((i, j))
            else:
                filled.append((i, j))
    H = len(hollow)
    F = len(filled)
    blocks = max(H, F)
    out = [[0] * 8 for _ in range(blocks * 4)]
    for idx in range(blocks):
        if idx < H:
            ii, jj = hollow[idx]
            for di in range(4):
                for dj in range(4):
                    out[idx*4 + di][dj] = grid[ii+di][jj+dj]
        if idx < F:
            ii, jj = filled[idx]
            for di in range(4):
                for dj in range(4):
                    out[idx*4 + di][4 + dj] = grid[ii+di][jj+dj]
    return out