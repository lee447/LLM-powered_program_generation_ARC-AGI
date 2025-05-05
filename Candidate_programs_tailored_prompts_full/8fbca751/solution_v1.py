from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    if h == 0:
        return grid
    w = len(grid[0])
    visited = [[False] * w for _ in range(h)]
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 8 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                coords = [(i, j)]
                while stack:
                    ci, cj = stack.pop()
                    for di, dj in dirs:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and grid[ni][nj] == 8:
                            visited[ni][nj] = True
                            stack.append((ni, nj))
                            coords.append((ni, nj))
                minr = min(r for r, c in coords)
                maxr = max(r for r, c in coords)
                minc = min(c for r, c in coords)
                maxc = max(c for r, c in coords)
                for r in range(minr, maxr + 1):
                    for c in range(minc, maxc + 1):
                        if grid[r][c] == 0:
                            grid[r][c] = 2
    return grid