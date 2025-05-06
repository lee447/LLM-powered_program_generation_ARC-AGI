from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    for sr in range(1, h, 6):
        if sr + 4 >= h: break
        for sc in range(1, w, 6):
            if sc + 4 >= w: break
            c = grid[sr][sc+1]
            ok = True
            for j in range(sc+1, sc+5):
                if grid[sr][j] != c or grid[sr+4][j] != c:
                    ok = False
            for i in range(sr+1, sr+5):
                if grid[i][sc] != c or grid[i][sc+4] != c:
                    ok = False
            for i in range(sr+1, sr+4):
                for j in range(sc+1, sc+4):
                    if grid[i][j] != 0:
                        ok = False
            if ok:
                for j in range(sc+1, sc+4):
                    res[sr+2][j] = c
                for i in range(sr+1, sr+4):
                    res[i][sc+2] = c
    return res