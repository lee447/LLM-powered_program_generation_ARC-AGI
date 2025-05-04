from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    pos5 = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==5]
    if not pos5:
        return grid
    r5_min = min(r for r,c in pos5)
    r5_max = max(r for r,c in pos5)
    c5_min = min(c for r,c in pos5)
    c5_max = max(c for r,c in pos5)
    hor_exists = False
    for r in range(r5_min, r5_max+1):
        cnt = sum(1 for c in range(w) if grid[r][c]==5)
        if cnt>1:
            hor_exists = True
            row_h = r
            cols = [c for c in range(w) if grid[r][c]==5]
            c5_min_hor = min(cols)
            c5_max_hor = max(cols)
            break
    vert_exists = False
    for c in range(c5_min, c5_max+1):
        cnt = sum(1 for r in range(h) if grid[r][c]==5)
        if cnt>1:
            vert_exists = True
            col_v = c
            rows = [r for r in range(h) if grid[r][c]==5]
            r5_min_vert = min(rows)
            r5_max_vert = max(rows)
            break
    visited = [[False]*w for _ in range(h)]
    blocks = []
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=0 and grid[r][c]!=5 and not visited[r][c]:
                queue = [(r,c)]
                visited[r][c] = True
                cells = [(r,c)]
                for rr,cc in queue:
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]!=0 and grid[nr][nc]!=5:
                            visited[nr][nc] = True
                            queue.append((nr,nc))
                            cells.append((nr,nc))
                r0 = min(rr for rr,cc in cells)
                r1 = max(rr for rr,cc in cells)
                c0 = min(cc for rr,cc in cells)
                c1 = max(cc for rr,cc in cells)
                vals = [[grid[ri][ci] for ci in range(c0,c1+1)] for ri in range(r0,r1+1)]
                blocks.append((r0,r1,c0,c1,vals))
    out = [row[:] for row in grid]
    for r0,r1,c0,c1,vals in blocks:
        touched = False
        if vert_exists:
            if c0-1==col_v and not touched and not (r1<r5_min_vert or r0>r5_max_vert):
                touched = True
                fill_r0 = min(r5_min_vert, r0)
                fill_r1 = max(r5_max_vert, r1)
                fill_c0 = c0
                fill_c1 = c1
            if c1+1==col_v and not touched and not (r1<r5_min_vert or r0>r5_max_vert):
                touched = True
                fill_r0 = min(r5_min_vert, r0)
                fill_r1 = max(r5_max_vert, r1)
                fill_c0 = c0
                fill_c1 = c1
        if hor_exists:
            if r0-1==row_h and not touched and not (c1<c5_min_hor or c0>c5_max_hor):
                touched = True
                fill_r0 = r0
                fill_r1 = r1
                fill_c0 = min(c5_min_hor, c0)
                fill_c1 = max(c5_max_hor, c1)
            if r1+1==row_h and not touched and not (c1<c5_min_hor or c0>c5_max_hor):
                touched = True
                fill_r0 = r0
                fill_r1 = r1
                fill_c0 = min(c5_min_hor, c0)
                fill_c1 = max(c5_max_hor, c1)
        if not touched:
            continue
        bh = r1 - r0 + 1
        bw = c1 - c0 + 1
        for i in range(fill_r0, fill_r1+1):
            for j in range(fill_c0, fill_c1+1):
                if out[i][j]==0:
                    vi = (i-r0) % bh
                    vj = (j-c0) % bw
                    out[i][j] = vals[vi][vj]
    return out