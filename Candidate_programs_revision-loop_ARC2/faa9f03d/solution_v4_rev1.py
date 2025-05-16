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
                        k = start - 1
                        while k >= 0 and res[i][k] == 0:
                            res[i][k] = c
                            k -= 1
                        k = end + 1
                        while k < w and res[i][k] == 0:
                            res[i][k] = c
                            k += 1
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
                        k = start - 1
                        while k >= 0 and res[k][j] == 0:
                            res[k][j] = c
                            k -= 1
                        k = end + 1
                        while k < h and res[k][j] == 0:
                            res[k][j] = c
                            k += 1
                else:
                    i += 1
    return res