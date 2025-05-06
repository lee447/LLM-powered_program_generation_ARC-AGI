from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    freq = {}
    for i in range(n):
        for j in range(n):
            freq[grid[i][j]] = freq.get(grid[i][j], 0) + 1
    min_count = min(freq.values())
    rare = {v for v, c in freq.items() if c == min_count}
    size = n * n
    out = [[0] * size for _ in range(size)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] in rare:
                br, bc = i * n, j * n
                for di in range(n):
                    for dj in range(n):
                        out[br + di][bc + dj] = grid[di][dj]
    return out