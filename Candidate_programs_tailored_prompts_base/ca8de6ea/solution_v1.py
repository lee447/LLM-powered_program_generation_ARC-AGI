from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    N = len(grid)
    c = N // 2
    M = c + 1
    c_out = M // 2
    out = [[0] * M for _ in range(M)]
    for i in range(N):
        for j in range(N):
            v = grid[i][j]
            if v == 0:
                continue
            dx = i - c
            dy = j - c
            k = max(abs(dx), abs(dy))
            if dx > 0:
                sdx = 1
            elif dx < 0:
                sdx = -1
            else:
                sdx = 0
            if dy > 0:
                sdy = 1
            elif dy < 0:
                sdy = -1
            else:
                sdy = 0
            if k == 0:
                oi, oj = c_out, c_out
            elif i == j:
                if k == c:
                    oi, oj = c_out + sdx, c_out + sdy
                else:
                    oi, oj = c_out + sdx, c_out
            elif i + j == N - 1:
                if k == c:
                    oi, oj = c_out + sdx, c_out + sdy
                else:
                    oi, oj = c_out, c_out + sdy
            else:
                continue
            out[oi][oj] = v
    return out