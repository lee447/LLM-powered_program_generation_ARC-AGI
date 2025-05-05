from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    min_r, max_r, min_c, max_c = rows, -1, cols, -1
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                if i < min_r: min_r = i
                if i > max_r: max_r = i
                if j < min_c: min_c = j
                if j > max_c: max_c = j
    result = []
    for i in range(min_r, min_r + 4):
        result.append(grid[i][min_c:min_c + 4])
    return result