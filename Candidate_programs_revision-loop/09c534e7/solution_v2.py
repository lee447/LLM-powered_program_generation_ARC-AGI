from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    zone = [[-1]*w for _ in range(h)]
    comps = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                cid = len(comps)
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                anchor = None
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    if grid[r][c] > 1:
                        anchor = grid[r][c]
                    zone[r][c] = cid
                    for dr,dc in dirs:
                        nr,nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                comps.append((cells, anchor))
    newg = [row[:] for row in grid]
    for cells, anchor in comps:
        if anchor is not None:
            for r,c in cells:
                newg[r][c] = anchor
        else:
            for r,c in cells:
                newg[r][c] = 1
    for cid, (cells, anchor) in enumerate(comps):
        if anchor is None:
            continue
        bc = anchor + 1
        for r,c in cells:
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if 0 <= nr < h and 0 <= nc < w:
                    if grid[nr][nc] != 0 and zone[nr][nc] != cid and newg[nr][nc] == 1:
                        newg[nr][nc] = bc
    return newg