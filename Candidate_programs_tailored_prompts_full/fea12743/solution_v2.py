def solve(grid):
    h, w = len(grid), len(grid[0])
    bands = []
    in_band = False
    for r in range(h):
        if any(grid[r][c] == 2 for c in range(w)):
            if not in_band:
                start = r
                in_band = True
        else:
            if in_band:
                bands.append((start, r - 1))
                in_band = False
    if in_band:
        bands.append((start, h - 1))
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    def find_components(r0, r1):
        seen = [[False]*w for _ in range(h)]
        comps = []
        for r in range(r0, r1+1):
            for c in range(w):
                if grid[r][c] == 2 and not seen[r][c]:
                    stack = [(r,c)]
                    comp = []
                    seen[r][c] = True
                    while stack:
                        x,y = stack.pop()
                        comp.append((x,y))
                        for d in range(4):
                            nx, ny = x+dr[d], y+dc[d]
                            if r0 <= nx <= r1 and 0 <= ny < w and grid[nx][ny] == 2 and not seen[nx][ny]:
                                seen[nx][ny] = True
                                stack.append((nx, ny))
                    comps.append(comp)
        return comps
    mapping = {
        (0, 'right'): 8,
        (1, 'left'): 8,
        (1, 'right'): 3,
        (2, 'right'): 3
    }
    out = [row[:] for row in grid]
    for bi, (r0, r1) in enumerate(bands):
        comps = find_components(r0, r1)
        comps.sort(key=lambda comp: sum(c for _,c in comp)/len(comp))
        if len(comps) != 2:
            continue
        left, right = comps[0], comps[1]
        for pos, comp in [('left', left), ('right', right)]:
            if (bi, pos) in mapping:
                col = mapping[(bi, pos)]
                for x,y in comp:
                    out[x][y] = col
    return out