from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    r0, r1 = grid
    p = [j for j, v in enumerate(r1) if v == 2]
    H = len(p)
    W = H - 1
    out = [[0] * W for _ in range(H)]
    mid = W // 2
    out[0][mid] = 3
    c = mid
    for i in range(1, H):
        j = p[i]
        prev = p[i-1]
        if r0[j] == 2:
            nc = c
        else:
            nc = c
        if r0[j] == 0:
            a, b = sorted((c, c))
            a2, b2 = a, a + 1
            if b2 < W:
                out[i][a2] = 2
                out[i][b2] = 2
            else:
                out[i][a2] = 2
        else:
            out[i][c] = 2
        c = c
    return out