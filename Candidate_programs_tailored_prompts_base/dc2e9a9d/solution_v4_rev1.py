from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0]) if H else 0
    ans = [row[:] for row in grid]
    squares = []
    for s in (3, 5):
        for i in range(H - s + 1):
            for j in range(W - s + 1):
                ok = True
                for k in range(s):
                    if grid[i][j+k] != 3 or grid[i+s-1][j+k] != 3 or grid[i+k][j] != 3 or grid[i+k][j+s-1] != 3:
                        ok = False
                        break
                if not ok:
                    continue
                for di in range(1, s-1):
                    for dj in range(1, s-1):
                        if grid[i+di][j+dj] == 3:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    squares.append((i, j, s))
    squares.sort(key=lambda x: (x[0], x[1]))
    for idx, (i, j, s) in enumerate(squares):
        col = 8 if idx == len(squares) - 1 else 1
        for di in range(1, s-1):
            for dj in range(1, s-1):
                ans[i+di][j+dj] = col
    return ans