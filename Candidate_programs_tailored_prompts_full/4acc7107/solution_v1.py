def solve(grid):
    h = len(grid)
    w = len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps_by_color = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v and not visited[r][c]:
                stack = [(r,c)]
                visited[r][c] = True
                comp = []
                while stack:
                    i,j = stack.pop()
                    comp.append((i,j))
                    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                        ni,nj = i+di, j+dj
                        if 0<=ni<h and 0<=nj<w and not visited[ni][nj] and grid[ni][nj]==v:
                            visited[ni][nj] = True
                            stack.append((ni,nj))
                comps_by_color.setdefault(v, []).append(comp)
    out = [[0]*w for _ in range(h)]
    gap = 1
    for v, comps in comps_by_color.items():
        if len(comps) != 2:
            continue
        comps.sort(key=lambda comp: -len(comp))
        a, b = comps
        # identify upper and lower by min row
        ra = min(r for r,_ in a)
        rb = min(r for r,_ in b)
        upper, lower = (a,b) if ra<rb else (b,a)
        min_ru = min(r for r,_ in upper)
        max_ru = max(r for r,_ in upper)
        min_rl = min(r for r,_ in lower)
        max_rl = max(r for r,_ in lower)
        shift_lower = (h-1) - max_rl
        lower_top = min_rl + shift_lower
        shift_upper = (lower_top - gap - 1) - max_ru
        for r,c in upper:
            out[r+shift_upper][c] = v
        for r,c in lower:
            out[r+shift_lower][c] = v
    return out