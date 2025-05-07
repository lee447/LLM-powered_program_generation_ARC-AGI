from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    row0, row1 = grid
    positions = [i for i, v in enumerate(row1) if v == 2]
    N = len(positions)
    M = N - 1
    out = [[0] * M for _ in range(N)]
    x = M // 2
    y = 0
    out[0][x] = 3
    for j in positions[:-1]:
        y += 1
        out[y][x] = 2
        if row0[j] == 2:
            if x + 1 < M:
                out[y][x + 1] = 2
            x += 1
        elif row0[j] == 0 and x + 1 < M:
            out[y][x + 1] = 2
    return out