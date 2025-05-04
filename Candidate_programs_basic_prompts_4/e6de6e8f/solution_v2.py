from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    row0, row1 = grid
    pos = [i for i in range(len(row0)) if row0[i] != 0 or row1[i] != 0]
    K = len(pos)
    start = pos[K//2] // 2
    out = [[0] * (K-1) for _ in range(K)]
    out[0][start] = 3
    prev = start
    for r in range(1, K):
        cur = (pos[r-1] + pos[r]) // 2
        c1, c2 = min(prev, cur), max(prev, cur)
        if c1 == c2:
            out[r][c1] = 2
        else:
            out[r][c1] = 2
            out[r][c2] = 2
        prev = cur
    return out