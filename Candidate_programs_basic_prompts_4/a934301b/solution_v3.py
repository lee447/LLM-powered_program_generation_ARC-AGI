from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    out = [[0]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                while stack:
                    r, c = stack.pop()
                    cells.append((r,c))
                    for dr, dc in dirs:
                        rr, cc = r+dr, c+dc
                        if 0 <= rr < h and 0 <= cc < w and not visited[rr][cc] and grid[rr][cc] != 0:
                            visited[rr][cc] = True
                            stack.append((rr,cc))
                rs = [r for r,c in cells]
                cs = [c for r,c in cells]
                minr, maxr = min(rs), max(rs)
                minc, maxc = min(cs), max(cs)
                height, width = maxr-minr+1, maxc-minc+1
                if height > 1 and width > 1 and height*width == len(cells):
                    cnt8 = sum(1 for r,c in cells if grid[r][c] == 8)
                    if cnt8 <= 1:
                        for r, c in cells:
                            out[r][c] = grid[r][c]
    return out