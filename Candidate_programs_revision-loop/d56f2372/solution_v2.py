from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    colors = {cell for row in grid for cell in row if cell != 0}
    for color in sorted(colors):
        minr, maxr, minc, maxc = rows, -1, cols, -1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == color:
                    if i < minr: minr = i
                    if i > maxr: maxr = i
                    if j < minc: minc = j
                    if j > maxc: maxc = j
        if maxr < 0: continue
        sub = []
        good = True
        for i in range(minr, maxr + 1):
            row = [(grid[i][j] if grid[i][j] == color else 0) for j in range(minc, maxc + 1)]
            if row != row[::-1]:
                good = False
                break
            sub.append(row)
        if good:
            return sub
    return []