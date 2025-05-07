from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    out = []
    for row in grid:
        expanded = []
        for v in row:
            expanded.extend([v, v])
        out.append(expanded)
        out.append(expanded.copy())
    return out