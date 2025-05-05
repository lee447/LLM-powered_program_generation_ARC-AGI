from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not vis[i][j]:
                stk = [(i, j)]
                vis[i][j] = True
                cells = []
                while stk:
                    y, x = stk.pop()
                    cells.append((y, x))
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] != 0 and not vis[ny][nx]:
                            vis[ny][nx] = True
                            stk.append((ny, nx))
                clusters.append(cells)
    out = [[0]*w for _ in range(h)]
    for cells in clusters:
        rows_with_8 = {r for r,c in cells if grid[r][c] == 8}
        if len(rows_with_8) <= 1:
            for r, c in cells:
                out[r][c] = grid[r][c]
    return out