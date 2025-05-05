from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    band_height = h // 3
    bands = [[], [], []]
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            if v != 0:
                idx = r // band_height
                if idx > 2:
                    idx = 2
                bands[idx].append((c, v))
    result = []
    for band in bands:
        band.sort(key=lambda x: x[0])
        result.append([v for _, v in band])
    return result