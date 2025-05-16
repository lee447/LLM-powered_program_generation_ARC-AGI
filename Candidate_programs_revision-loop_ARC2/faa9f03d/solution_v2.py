from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    colors = {c for row in grid for c in row if c != 0}
    for c in colors:
        for i in range(h):
            j = 0
            while j < w:
                if grid[i][j] == c:
                    start = j
                    while j < w and grid[i][j] == c:
                        j += 1
                    end = j - 1
                    if end - start + 1 >= 2:
                        if start - 1 >= 0 and res[i][start - 1] == 0:
                            res[i][start - 1] = c
                        if end + 1 < w and res[i][end + 1] == 0:
                            res[i][end + 1] = c
                else:
                    j += 1
        for j in range(w):
            i = 0
            while i < h:
                if grid[i][j] == c:
                    start = i
                    while i < h and grid[i][j] == c:
                        i += 1
                    end = i - 1
                    if end - start + 1 >= 2:
                        if start - 1 >= 0 and res[start - 1][j] == 0:
                            res[start - 1][j] = c
                        if end + 1 < h and res[end + 1][j] == 0:
                            res[end + 1][j] = c
                else:
                    i += 1
    return res