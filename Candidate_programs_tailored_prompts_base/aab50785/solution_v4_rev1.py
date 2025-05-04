from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    anchors = []
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j] == grid[i][j+1] == grid[i+1][j] == grid[i+1][j+1] == 8:
                anchors.append((i, j))
    row_map = {}
    for i, j in anchors:
        row_map.setdefault(i, []).append(j)
    result = []
    for i in sorted(row_map):
        js = sorted(row_map[i])
        j1, j2 = js[0], js[1]
        start, end = j1 + 2, j2 - 1
        result.append(grid[i][start:end+1])
        result.append(grid[i+1][start:end+1])
    return result