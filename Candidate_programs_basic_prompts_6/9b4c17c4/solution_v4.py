def solve(grid):
    h = len(grid)
    w = len(grid[0])
    bgs = {v for row in grid for v in row if v != 2}
    bg_list = list(bgs)
    horizontal = True
    for row in grid:
        s = {v for v in row if v != 2}
        if len(s) > 1:
            horizontal = False
            break
    if horizontal:
        first_bg = next(v for v in grid[0] if v != 2)
        split = 0
        for i, row in enumerate(grid):
            s = {v for v in row if v != 2}
            if s and next(iter(s)) != first_bg:
                split = i
                break
        other_bg = next(x for x in bg_list if x != first_bg)
        regions = [
            (0, split - 1, 0, w - 1, first_bg),
            (split, h - 1, 0, w - 1, other_bg)
        ]
    else:
        first_bg = next(grid[i][0] for i in range(h) if grid[i][0] != 2)
        split = 0
        for j in range(w):
            s = {grid[i][j] for i in range(h) if grid[i][j] != 2}
            if s and next(iter(s)) != first_bg:
                split = j
                break
        other_bg = next(x for x in bg_list if x != first_bg)
        regions = [
            (0, h - 1, 0, split - 1, first_bg),
            (0, h - 1, split, w - 1, other_bg)
        ]
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for ri, (r0, r1, c0, c1, bg) in enumerate(regions):
        for r in range(r0, r1+1):
            for c in range(c0, c1+1):
                if grid[r][c] == 2 and not visited[r][c]:
                    stack = [(r, c)]
                    comp = []
                    visited[r][c] = True
                    while stack:
                        x, y = stack.pop()
                        comp.append((x, y))
                        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            nx, ny = x+dx, y+dy
                            if r0 <= nx <= r1 and c0 <= ny <= c1 and not visited[nx][ny] and grid[nx][ny] == 2:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                    clusters.append((ri, comp))
    new_grid = [row[:] for row in grid]
    for ri, comp in clusters:
        _, _, c0, _, bg = regions[ri]
        for r, c in comp:
            new_grid[r][c] = bg
    for ri, comp in clusters:
        r0, r1, c0, c1, bg = regions[ri]
        other_bg = regions[1-ri][4]
        minc = min(c for _, c in comp)
        maxc = max(c for _, c in comp)
        if bg < other_bg:
            dx = c1 - maxc
        else:
            dx = c0 - minc
        for r, c in comp:
            new_grid[r][c+dx] = 2
    return new_grid