def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
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
                    for dr,dc in dirs:
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]!=bg:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                minr = min(r for r,c in cells)
                minc = min(c for r,c in cells)
                shape = {(r-minr,c-minc):grid[r][c] for r,c in cells}
                shapes.append((minr,minc,shape))
    shapes.sort()
    n = len(shapes)
    res = [row[:] for row in grid]
    for idx, (r0,c0,shape) in enumerate(shapes):
        _,_,next_shape = shapes[(idx+1)%n]
        for (dr,dc),col in next_shape.items():
            r,c = r0+dr, c0+dc
            res[r][c] = col
    return res