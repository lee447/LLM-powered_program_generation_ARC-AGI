from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    pts = [(i, j) for i in range(h) for j in range(w) if grid[i][j] != 0]
    if not pts:
        return grid
    min_r = min(i for i, _ in pts)
    max_r = max(i for i, _ in pts)
    min_c = min(j for _, j in pts)
    max_c = max(j for _, j in pts)
    S0 = [row[min_c:max_c+1] for row in grid[min_r:max_r+1]]
    def rotate(mat):
        H, W = len(mat), len(mat[0])
        R = [[0]*H for _ in range(W)]
        for i in range(H):
            for j in range(W):
                R[j][H-1-i] = mat[i][j]
        return R
    S1 = rotate(S0)
    S2 = rotate(S1)
    S3 = rotate(S2)
    shapes = [S0, S1, S2, S3]
    sh_dims = [(len(s), len(s[0])) for s in shapes]
    b = max(sh_dims[0][0], sh_dims[0][1])
    N = 3*b if b%2 else 3*b-1
    res = [[0]*N for _ in range(N)]
    c = N//2
    # Up
    h0, w0 = sh_dims[0]
    i0, j0 = 0, c - w0//2
    for i in range(h0):
        for j in range(w0):
            if shapes[0][i][j] != 0:
                res[i0+i][j0+j] = shapes[0][i][j]
    # Right
    h1, w1 = sh_dims[1]
    i1, j1 = c - h1//2, N - w1
    for i in range(h1):
        for j in range(w1):
            if shapes[1][i][j] != 0:
                res[i1+i][j1+j] = shapes[1][i][j]
    # Down
    h2, w2 = sh_dims[2]
    i2, j2 = N - h2, c - w2//2
    for i in range(h2):
        for j in range(w2):
            if shapes[2][i][j] != 0:
                res[i2+i][j2+j] = shapes[2][i][j]
    # Left
    h3, w3 = sh_dims[3]
    i3, j3 = c - h3//2, 0
    for i in range(h3):
        for j in range(w3):
            if shapes[3][i][j] != 0:
                res[i3+i][j3+j] = shapes[3][i][j]
    return res