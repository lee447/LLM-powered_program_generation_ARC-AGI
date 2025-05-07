from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    k = len({x for row in grid for x in row})
    res = []
    for _ in range(k):
        for row in grid:
            new_row = []
            for _ in range(k):
                new_row += row
            res.append(new_row)
    return res