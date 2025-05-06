from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    C = None
    for row in grid:
        for v in row:
            if v != 0:
                C = v
                break
        if C is not None:
            break
    fill = {3: 1, 5: 4, 8: 2}.get(C, 1)
    return [[0 if v == C else fill for v in row] for row in grid]