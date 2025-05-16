def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs4 = [(1,0),(-1,0),(0,1),(0,-1)]
    dirs8 = [(dr,dc) for dr in (-1,0,1) for dc in (-1,0,1) if not (dr==0 and dc==0)]
    # find red (2) components
    visited = [[False]*W for _ in range(H)]
    red_comps = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 2 and not visited[r][c]:
                comp = []
                stack = [(r,c)]
                visited[r][c] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs4:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == 2:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                red_comps.append(comp)
    out = [row[:] for row in grid]
    # BFS8 for shape
    def bfs_shape(sr, sc, val):
        comp = []
        q = [(sr,sc)]
        seen = { (sr,sc) }
        while q:
            x,y = q.pop()
            comp.append((x,y))
            for dx,dy in dirs8:
                nx, ny = x+dx, y+dy
                if 0 <= nx < H and 0 <= ny < W and (nx,ny) not in seen and grid[nx][ny] == val:
                    seen.add((nx,ny))
                    q.append((nx,ny))
        return comp
    for comp in red_comps:
        if len(comp) == 1:
            r0,c0 = comp[0]
            seed = None
            for dr,dc in dirs8:
                nr, nc = r0+dr, c0+dc
                if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] not in (1,2):
                    seed = (nr,nc)
                    break
            if seed is None:
                continue
            val = grid[seed[0]][seed[1]]
            shape = bfs_shape(seed[0], seed[1], val)
            for r,c in shape:
                rr, cc = 2*r0 - r, 2*c0 - c
                if 0 <= rr < H and 0 <= cc < W and out[rr][cc] == 1:
                    out[rr][cc] = val
        else:
            rows = {r for r,c in comp}
            cols = {c for r,c in comp}
            if len(rows) == 1:
                # horizontal axis
                r0 = next(iter(rows))
                seed = None
                dirv = None
                for r,c in comp:
                    for dr,dc,dv in [( -1,0,'up'),(1,0,'down')]:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] not in (1,2):
                            seed = (nr,nc)
                            dirv = dv
                            break
                    if seed: break
                if seed is None: continue
                val = grid[seed[0]][seed[1]]
                shape = bfs_shape(seed[0], seed[1], val)
                if dirv == 'up':
                    for r,c in shape:
                        if r < r0:
                            rr, cc = 2*r0 - r, c
                            if 0 <= rr < H and 0 <= cc < W and out[rr][cc] == 1:
                                out[rr][cc] = val
                else:
                    for r,c in shape:
                        if r > r0:
                            rr, cc = 2*r0 - r, c
                            if 0 <= rr < H and 0 <= cc < W and out[rr][cc] == 1:
                                out[rr][cc] = val
            elif len(cols) == 1:
                # vertical axis
                c0 = next(iter(cols))
                seed = None
                dirv = None
                for r,c in comp:
                    for dr,dc,dv in [(0,-1,'left'),(0,1,'right')]:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] not in (1,2):
                            seed = (nr,nc)
                            dirv = dv
                            break
                    if seed: break
                if seed is None: continue
                val = grid[seed[0]][seed[1]]
                shape = bfs_shape(seed[0], seed[1], val)
                if dirv == 'left':
                    for r,c in shape:
                        if c < c0:
                            rr, cc = r, 2*c0 - c
                            if 0 <= rr < H and 0 <= cc < W and out[rr][cc] == 1:
                                out[rr][cc] = val
                else:
                    for r,c in shape:
                        if c > c0:
                            rr, cc = r, 2*c0 - c
                            if 0 <= rr < H and 0 <= cc < W and out[rr][cc] == 1:
                                out[rr][cc] = val
    return out