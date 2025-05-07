def solve(grid):
    h_tot = len(grid)
    w_tot = len(grid[0])
    five_rows = sorted({r for r in range(h_tot) for c in range(w_tot) if grid[r][c] == 5})
    groups = []
    for r in five_rows:
        if not groups or r != groups[-1][-1] + 1:
            groups.append([])
        groups[-1].append(r)
    block_h = len(groups[0])
    row_starts = [g[0] for g in groups]
    sep_h = row_starts[1] - row_starts[0] - block_h if len(row_starts) > 1 else 1
    five_cols = sorted({c for r in five_rows for c in range(w_tot) if grid[r][c] == 5})
    cgroups = []
    for c in five_cols:
        if not cgroups or c != cgroups[-1][-1] + 1:
            cgroups.append([])
        cgroups[-1].append(c)
    block_w = len(cgroups[0])
    col_starts = [g[0] for g in cgroups]
    sep_w = col_starts[1] - col_starts[0] - block_w if len(col_starts) > 1 else 1
    top_end = row_starts[0]
    colored = [(r,c,grid[r][c]) for r in range(top_end) for c in range(w_tot) if grid[r][c] > 1 and grid[r][c] != 5]
    ones = [(r,c) for r in range(top_end) for c in range(w_tot) if grid[r][c] == 1]
    visited = set()
    shapes = {}
    for oy,ox in ones:
        if (oy,ox) in visited: continue
        stack = [(oy,ox)]
        comp = []
        visited.add((oy,ox))
        while stack:
            y,x = stack.pop()
            comp.append((y,x))
            for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                ny,nx = y+dy, x+dx
                if 0 <= ny < top_end and 0 <= nx < w_tot and grid[ny][nx] == 1 and (ny,nx) not in visited:
                    visited.add((ny,nx))
                    stack.append((ny,nx))
        miny = min(y for y,x in comp)
        minx = min(x for y,x in comp)
        offsets = [(y-miny, x-minx) for y,x in comp]
        for cy,cx,val in colored:
            if cx + 1 == minx:
                shapes[val] = offsets
                break
    M = len(row_starts)
    N = len(col_starts)
    out_h = M*block_h + (M-1)*sep_h
    out_w = N*block_w + (N-1)*sep_w
    out = [[0]*out_w for _ in range(out_h)]
    for i, br in enumerate(row_starts):
        for j, bc in enumerate(col_starts):
            cy = br + 1
            cx = bc + 1
            color = grid[cy][cx]
            if color != 5:
                so = shapes.get(color, [])
                oy = i*(block_h+sep_h)
                ox = j*(block_w+sep_w)
                for dy,dx in so:
                    out[oy+dy][ox+dx] = color
    return out