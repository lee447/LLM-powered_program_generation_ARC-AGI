from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    clusters = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i, j)]
                comp = []
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c, grid[r][c]))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] != 0:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                clusters.append(comp)
    main = None
    anchor = None
    for comp in clusters:
        if len(comp) > 1:
            main = comp
        else:
            if comp[0][2] == 5:
                anchor = comp[0]
    orig_r_grey, orig_c_grey = next((r,c) for (r,c,v) in main if v == 5)
    anchor_r, anchor_c, _ = anchor
    dr, dc = anchor_r - orig_r_grey, anchor_c - orig_c_grey
    output = [row[:] for row in grid]
    for r, c, v in main:
        nr, nc = r + dr, c + dc
        output[nr][nc] = v
    return output