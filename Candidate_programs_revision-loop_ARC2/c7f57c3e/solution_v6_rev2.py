from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    dirs8 = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    seen = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != bg and not seen[i][j]:
                stack = [(i,j)]
                seen[i][j] = True
                cells = []
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    for dr,dc in dirs8:
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]!=bg:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                minr = min(r for r,c in cells)
                minc = min(c for r,c in cells)
                shape = {(r-minr,c-minc): grid[r][c] for r,c in cells}
                shapes.append((minr, minc, cells, shape))
    groups = {}
    for idx,(r0,c0,cells,shape) in enumerate(shapes):
        dims = (max(r for r,c in cells)-min(r for r,c in cells),
                max(c for r,c in cells)-min(c for r,c in cells))
        groups.setdefault(dims, []).append(idx)
    res = [row[:] for row in grid]
    for grp in groups.values():
        if len(grp)<2: continue
        k = len(grp)
        for i,idx in enumerate(sorted(grp, key=lambda x:shapes[x][0])):
            _,c0,_,shape = shapes[idx]
            _,nc0,_,nshape = shapes[grp[(i+1)%k]]
            cells_old = shapes[idx][2]
            h0 = max(r for r,c in cells_old)-min(r for r,c in cells_old)
            # trunk row and cluster row
            tr = shapes[idx][0] + h0 - 2
            cr = shapes[idx][0] + h0 - 1
            for (dr,dc),col in nshape.items():
                if dr in (h0-2,h0-1):
                    r = shapes[idx][0] + dr
                    c = shapes[idx][1] + dc
                    res[r][c] = col
    return res