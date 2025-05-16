from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    bar_x = 0
    for j in range(w):
        ok = True
        for i in range(h):
            if grid[i][j] != 2:
                ok = False
                break
        if ok:
            bar_x = j
            break
    out = [row[:] for row in grid]
    for i in range(h):
        j = 0
        while j < bar_x:
            if grid[i][j] != 0:
                C = grid[i][j]
                L = 1
                while j + L < bar_x and grid[i][j + L] == C:
                    L += 1
                k = 0
                while True:
                    pos = bar_x + 1 + k * L
                    if pos >= w:
                        break
                    out[i][pos] = C
                    k += 1
                j += L
            else:
                j += 1
    return out