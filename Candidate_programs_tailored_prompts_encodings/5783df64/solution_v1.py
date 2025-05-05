from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    t = h // 3
    bands = [[], [], []]
    for i in range(h):
        for j, v in enumerate(grid[i]):
            if v != 0:
                idx = i // t
                if idx > 2:
                    idx = 2
                bands[idx].append((j, v))
    result = []
    for band in bands:
        band.sort(key=lambda x: x[0])
        result.append([v for _, v in band])
    return result