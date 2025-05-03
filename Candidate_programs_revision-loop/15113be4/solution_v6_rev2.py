from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    sep_rows = [i for i in range(H) if all(grid[i][j] == 4 for j in range(W))]
    sep_cols = [j for j in range(W) if all(grid[i][j] == 4 for i in range(H))]
    row_bounds = []
    prev = 0
    for r in sep_rows:
        row_bounds.append((prev, r))
        prev = r + 1
    row_bounds.append((prev, H))
    col_bounds = []
    prev = 0
    for c in sep_cols:
        col_bounds.append((prev, c))
        prev = c + 1
    col_bounds.append((prev, W))
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def signature(cells):
        ys = [y for y,_ in cells]
        xs = [x for _,x in cells]
        my, mx = min(ys), min(xs)
        return tuple(sorted(((y-my, x-mx) for y,x in cells)))
    for r0, r1 in row_bounds:
        for c0, c1 in col_bounds:
            comps_color = []
            comps_mask = []
            seen = [[False]*W for _ in range(H)]
            for i in range(r0, r1):
                for j in range(c0, c1):
                    if not seen[i][j] and grid[i][j] not in (0,1,4):
                        col = grid[i][j]
                        q = deque([(i,j)])
                        seen[i][j] = True
                        cells = []
                        while q:
                            y,x = q.popleft()
                            cells.append((y,x))
                            for dy,dx in dirs:
                                ny, nx = y+dy, x+dx
                                if r0<=ny<r1 and c0<=nx<c1 and not seen[ny][nx] and grid[ny][nx]==col:
                                    seen[ny][nx] = True
                                    q.append((ny,nx))
                        comps_color.append((cells,col,signature(cells)))
            seen = [[False]*W for _ in range(H)]
            for i in range(r0, r1):
                for j in range(c0, c1):
                    if not seen[i][j] and grid[i][j] == 1:
                        q = deque([(i,j)])
                        seen[i][j] = True
                        cells = []
                        while q:
                            y,x = q.popleft()
                            cells.append((y,x))
                            for dy,dx in dirs:
                                ny, nx = y+dy, x+dx
                                if r0<=ny<r1 and c0<=nx<c1 and not seen[ny][nx] and grid[ny][nx]==1:
                                    seen[ny][nx] = True
                                    q.append((ny,nx))
                        comps_mask.append((cells,signature(cells)))
            mask_dict = {sig:cells for cells,sig in comps_mask}
            for cells,col,sig in comps_color:
                if sig in mask_dict:
                    m_cells = mask_dict[sig]
                    for y,x in cells:
                        grid[y][x] = 1
                    for y,x in m_cells:
                        grid[y][x] = col
    return grid