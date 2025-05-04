def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def flood(start_r, start_c, color, visited):
        stack = [(start_r, start_c)]
        comp = []
        visited.add((start_r, start_c))
        while stack:
            r,c = stack.pop()
            comp.append((r,c))
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if 0<=nr<H and 0<=nc<W and (nr,nc) not in visited and grid[nr][nc]==color:
                    visited.add((nr,nc))
                    stack.append((nr,nc))
        return comp
    visited = set()
    anchor = []
    for i in range(H):
        for j in range(W):
            if grid[i][j]==4 and (i,j) not in visited:
                anchor = flood(i,j,4,visited)
                break
        if anchor:
            break
    ars = [(r-min(r for r,c in anchor), c-min(c for r,c in anchor)) for r,c in anchor]
    transforms = [
        lambda r,c:( r, c), lambda r,c:( r,-c),
        lambda r,c:(-r, c), lambda r,c:(-r,-c),
        lambda r,c:( c, r), lambda r,c:( c,-r),
        lambda r,c:(-c, r), lambda r,c:(-c,-r)
    ]
    norm_shapes = []
    for f in transforms:
        tpts = [f(r,c) for r,c in ars]
        minr = min(r for r,c in tpts); minc = min(c for r,c in tpts)
        norm_shapes.append(set((r-minr,c-minc) for r,c in tpts))
    new_grid = [row[:] for row in grid]
    visited6 = set()
    for i in range(H):
        for j in range(W):
            if grid[i][j]==6 and (i,j) not in visited6:
                comp = flood(i,j,6,visited6)
                if len(comp)==len(ars):
                    minr = min(r for r,c in comp); minc = min(c for r,c in comp)
                    offs = set((r-minr,c-minc) for r,c in comp)
                    if any(offs==shape for shape in norm_shapes):
                        for r,c in comp:
                            new_grid[r][c] = 4
    return new_grid