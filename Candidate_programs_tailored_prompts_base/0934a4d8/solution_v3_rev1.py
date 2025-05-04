from typing import List, Tuple

def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    rows, cols = [], []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 8:
                rows.append(i)
                cols.append(j)
    r0, r1 = min(rows), max(rows)
    c0, c1 = min(cols), max(cols)
    H, W = r1 - r0 + 1, c1 - c0 + 1
    freq = {}
    for i in range(n - H + 1):
        for j in range(m - W + 1):
            block = []
            skip = False
            for di in range(H):
                for dj in range(W):
                    v = grid[i+di][j+dj]
                    if v == 8:
                        skip = True
                        break
                    block.append(v)
                if skip:
                    break
            if not skip:
                key = tuple(block)
                freq[key] = freq.get(key, 0) + 1
    best = max(freq.items(), key=lambda x: x[1])[0]
    return [list(best[i*W:(i+1)*W]) for i in range(H)]