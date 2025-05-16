def solve(grid):
    h, w = len(grid), len(grid[0])
    cols = set(c for r in range(h) for c in range(w) if grid[r][c]==4)
    min_barrier, max_barrier = min(cols), max(cols)
    left_bg = grid[0][min_barrier-1]
    right_bg = grid[0][max_barrier+1]
    shape = [(r,c,grid[r][c]) for r in range(h) for c in range(min_barrier) 
             if grid[r][c] not in (left_bg,1,2,4)]
    top, bottom = min(r for r,_,_ in shape), max(r for r,_,_ in shape)
    mid_zone = (0 + h-1)//2
    shape_mid = (top+bottom)//2
    dr = mid_zone - shape_mid
    out = [row[:] for row in grid]
    for r,c,v in shape:
        out[r][c] = left_bg
    for r,c,v in shape:
        nr = r + dr
        nc = (min_barrier-1)*2 - c + max_barrier+1 - min_barrier
        if 0<=nr<h and min_barrier<nc<w:
            out[nr][nc] = v
    return out