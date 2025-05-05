from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    visited = [[False]*C for _ in range(R)]
    clusters = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] != 0 and not visited[i][j]:
                comp = []
                stack = [(i, j)]
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c, grid[r][c]))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and grid[nr][nc] != 0:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                clusters.append(comp)
    main = next(comp for comp in clusters if len(comp) > 1)
    orig_r, orig_c = next((r, c) for r, c, v in main if v == 5)
    anchors = [(r, c) for comp in clusters if len(comp) == 1 and comp[0][2] == 5 for r, c, _ in [comp[0]]]
    anchor_r, anchor_c = next((r, c) for r, c in anchors if (r, c) != (orig_r, orig_c))
    dr, dc = anchor_r - orig_r, anchor_c - orig_c
    output = [row[:] for row in grid]
    for r, c, v in main:
        if v != 5:
            nr, nc = r + dr, c + dc
            output[nr][nc] = v
    return output