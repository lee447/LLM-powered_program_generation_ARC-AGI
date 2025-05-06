from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 8 and not visited[i][j]:
                minr, maxr, minc, maxc = i, i, j, j
                stack = [(i,j)]
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    minr, maxr = min(minr, r), max(maxr, r)
                    minc, maxc = min(minc, c), max(maxc, c)
                    for dr in (-1,0,1):
                        for dc in (-1,0,1):
                            nr, nc = r+dr, c+dc
                            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == 8:
                                visited[nr][nc] = True
                                stack.append((nr,nc))
                clusters.append((minr, maxr, minc, maxc))
    res = [row[:] for row in grid]
    for minr, maxr, minc, maxc in clusters:
        for r in range(minr, maxr+1):
            for c in range(minc, maxc+1):
                if res[r][c] != 8:
                    res[r][c] = 2
    return res