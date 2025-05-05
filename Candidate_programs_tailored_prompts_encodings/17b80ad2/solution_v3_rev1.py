from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    new = [[0]*n for _ in range(m)]
    for j in range(n):
        anchors = [(i, grid[i][j]) for i in range(m) if grid[i][j] != 0]
        if len(anchors) < 2:
            for i, v in anchors:
                new[i][j] = v
        else:
            prev = -1
            for i, v in anchors:
                start = 0 if prev == -1 else prev + 1
                for r in range(start, i+1):
                    new[r][j] = v
                prev = i
    return new