from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    m = w // 3
    sums = []
    for i in range(3):
        s = sum(grid[r][c] for r in range(h) for c in range(i*m, (i+1)*m))
        sums.append((s, i))
    order = sorted(sums, key=lambda x: x[0])
    colors = [1,3,4,6,9]
    mapping = {}
    for k, (_, idx) in enumerate(order):
        mapping[idx] = colors[k]
    out = [[0]*w for _ in range(h)]
    for i in range(3):
        for r in range(h):
            for c in range(i*m, (i+1)*m):
                out[r][c] = mapping[i]
    return out