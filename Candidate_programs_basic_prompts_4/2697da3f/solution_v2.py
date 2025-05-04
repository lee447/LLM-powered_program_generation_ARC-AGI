def solve(grid):
    h, w = len(grid), len(grid[0])
    pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0]
    if not pts:
        return grid
    minr = min(r for r, c in pts)
    maxr = max(r for r, c in pts)
    minc = min(c for r, c in pts)
    maxc = max(c for r, c in pts)
    A = [row[minc:maxc+1] for row in grid[minr:maxr+1]]
    def rot(mat):
        return [[mat[len(mat) - 1 - r][c] for r in range(len(mat))] for c in range(len(mat[0]))]
    R0 = A
    R1 = rot(R0)
    R2 = rot(R1)
    R3 = rot(R2)
    br, bc = len(A), len(A[0])
    out = [[0] * (3 * bc) for _ in range(3 * br)]
    for (bi, bj), M in [((0, 1), R0), ((1, 2), R1), ((2, 1), R2), ((1, 0), R3)]:
        for r in range(len(M)):
            for c in range(len(M[0])):
                out[bi * br + r][bj * bc + c] = M[r][c]
    return out