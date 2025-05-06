from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    max_count = -1
    regions = []
    for i in range(h - 2):
        for j in range(w - 2):
            cnt = 0
            for di in range(3):
                for dj in range(3):
                    if grid[i+di][j+dj] == 6:
                        cnt += 1
            if cnt > max_count:
                max_count = cnt
                regions = [(i, j)]
            elif cnt == max_count:
                regions.append((i, j))
    res = [row[:] for row in grid]
    for i, j in regions:
        for di in range(3):
            for dj in range(3):
                if res[i+di][j+dj] != 6:
                    res[i+di][j+dj] = 4
    return res