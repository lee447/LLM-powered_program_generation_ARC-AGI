from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    visited = [[False] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if not visited[r][c] and grid[r][c] == 0:
                stack = [(r, c)]
                visited[r][c] = True
                comp = [(r, c)]
                while stack:
                    rr, cc = stack.pop()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = rr + dr, cc + dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == 0:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                            comp.append((nr, nc))
                if len(comp) >= 2:
                    for rr, cc in comp:
                        res[rr][cc] = 8
    return res