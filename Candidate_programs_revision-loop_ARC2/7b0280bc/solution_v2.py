def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    changes = {}
    for i in range(h-1):
        for j in range(w-1):
            c = grid[i][j]
            if c != bg and grid[i][j+1] == c and grid[i+1][j] == c and grid[i+1][j+1] == c:
                changes.setdefault(c, []).append((i, j))
    out = [row[:] for row in grid]
    for c, pos in changes.items():
        k = len(pos)
        if k == 2:
            col = 5 if c % 2 == 0 else 3
            for i, j in pos:
                for di in (0,1):
                    for dj in (0,1):
                        out[i+di][j+dj] = col
        elif k > 2:
            col = 5 if c % 2 == 0 else 3
            for i, j in pos[k//2:]:
                for di in (0,1):
                    for dj in (0,1):
                        out[i+di][j+dj] = col
    return out