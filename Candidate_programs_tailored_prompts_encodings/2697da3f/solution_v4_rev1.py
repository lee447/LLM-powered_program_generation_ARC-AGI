def solve(grid):
    n = len(grid)
    pts = [(r, c) for r in range(n) for c in range(len(grid[0])) if grid[r][c] != 0]
    if not pts:
        return grid
    rs = [r for r, _ in pts]
    cs = [c for _, c in pts]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    h = r1 - r0 + 1
    w = c1 - c0 + 1
    if h == w:
        sub = [row[c0:c1+1] for row in grid[r0:r1+1]]
        s = h
        dim = 3 * s
        G = [[0] * dim for _ in range(dim)]
        def rot(mat):
            m = len(mat)
            return [[mat[m-1-j][i] for j in range(m)] for i in range(m)]
        T = sub
        offs = [(0, s), (s, 2*s), (2*s, s), (s, 0)]
        for dx, dy in offs:
            for i in range(s):
                for j in range(s):
                    if T[i][j] != 0:
                        G[dx + i][dy + j] = T[i][j]
            T = rot(T)
        return G
    else:
        # diamond fractal
        size = min(h, w)
        r = size - 1
        dim = 4 * size - 1
        G = [[0] * dim for _ in range(dim)]
        center = dim // 2
        color = grid[r0 + h//2][c0 + w//2]
        shifts = [(-size, 0), (0, size), (size, 0), (0, -size)]
        for dx0, dy0 in shifts:
            cx, cy = center + dx0, center + dy0
            for di in range(-r, r+1):
                for dj in range(-r, r+1):
                    if abs(di) + abs(dj) <= r:
                        G[cx + di][cy + dj] = color
        return G