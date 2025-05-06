def solve(grid):
    n = len(grid)
    def rot_ccw(g):
        return [[g[j][n-1-i] for j in range(n)] for i in range(n)]
    def rot_cw(g):
        return [[g[n-1-j][i] for j in range(n)] for i in range(n)]
    def rot_180(g):
        return [row[::-1] for row in g[::-1]]
    g0 = grid
    g1 = rot_ccw(grid)
    g2 = rot_180(grid)
    g3 = rot_cw(grid)
    return [g0[i] + g1[i] for i in range(n)] + [g2[i] + g3[i] for i in range(n)]