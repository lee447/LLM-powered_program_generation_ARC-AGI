from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    if h == 0:
        return []
    w = len(grid[0])
    dirs = [(0,1),(1,0),(1,1),(1,-1)]
    best = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5:
                for di, dj in dirs:
                    if not (0 <= i-di < h and 0 <= j-dj < w and grid[i-di][j-dj] == 5):
                        length = 0
                        x, y = i, j
                        while 0 <= x < h and 0 <= y < w and grid[x][y] == 5:
                            length += 1
                            x += di
                            y += dj
                        if length > best:
                            best = length
    return [[0] for _ in range(best)]