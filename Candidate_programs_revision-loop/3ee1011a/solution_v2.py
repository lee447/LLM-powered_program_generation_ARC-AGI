from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    counts = {}
    for row in grid:
        for c in row:
            if c != 0:
                counts[c] = counts.get(c, 0) + 1
    items = sorted(counts.items(), key=lambda x: -x[1])
    N = items[0][1]
    colors = [c for c, _ in items]
    out = [[0] * N for _ in range(N)]
    for k, c in enumerate(colors):
        for i in range(k, N - k):
            out[k][i] = c
            out[N - 1 - k][i] = c
            out[i][k] = c
            out[i][N - 1 - k] = c
    return out