def solve(grid):
    h = len(grid)
    w = len(grid[0])
    wave1 = [-1, 0, 1, 0]
    wave2 = [0, 1, 0, -1]
    wave2_rev = [0, -1, 0, 1]
    horizontal = set()
    vertical = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 0:
                if c>0 and grid[r][c-1]!=0 or c<w-1 and grid[r][c+1]!=0:
                    horizontal.add(r)
                if r>0 and grid[r-1][c]!=0 or r<h-1 and grid[r+1][c]!=0:
                    vertical.add(c)
    h_list = sorted(horizontal)
    v_list = sorted(vertical)
    dx_h = {}
    nh = len(h_list)
    for j, r in enumerate(h_list):
        if nh == 2:
            dx = 0
        elif nh == 1:
            dx = -wave1[j % 4]
        else:
            dx = wave1[j % 4]
        dx_h[r] = dx
    v_rows = {}
    for c in v_list:
        lst = [r for r in range(h) if grid[r][c]!=0 and r not in horizontal]
        v_rows[c] = sorted(lst)
    dx_v = {}
    nv = len(v_list)
    for c, rows in v_rows.items():
        for i, r in enumerate(rows):
            if nv <= 2:
                dx = wave1[(i-1) % 4]
            else:
                if nh > 2:
                    dx = wave2[i % 4]
                else:
                    dx = wave2_rev[i % 4]
            dx_v[(r, c)] = dx
    out = [[0]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v == 0: continue
            if r in dx_h:
                nc = c + dx_h[r]
            elif (r, c) in dx_v:
                nc = c + dx_v[(r, c)]
            else:
                nc = c
            if 0 <= nc < w:
                out[r][nc] = v
    return out