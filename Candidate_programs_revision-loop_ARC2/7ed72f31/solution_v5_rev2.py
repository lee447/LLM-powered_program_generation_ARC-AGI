from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    vis = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if not vis[i][j]:
                color = grid[i][j]
                dq = deque([(i,j)])
                vis[i][j] = True
                comp = []
                while dq:
                    r, c = dq.popleft()
                    comp.append((r,c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not vis[nr][nc] and grid[nr][nc] == color:
                            vis[nr][nc] = True
                            dq.append((nr,nc))
                clusters.append((color, comp))
    pivot_idxs = [i for i,(color,comp) in enumerate(clusters) if color == 2]
    others = [(i,color,comp) for i,(color,comp) in enumerate(clusters) if color != bg and color != 2]
    out = [row[:] for row in grid]
    processed = set()
    for idx, color, comp in others:
        if idx in processed:
            continue
        found = False
        for pi in pivot_idxs:
            p = clusters[pi][1]
            for r,c in comp:
                for pr,pc in p:
                    if abs(r-pr)+abs(c-pc) == 1:
                        found = True
                        pivot = p
                        break
                if found:
                    break
            if found:
                break
        if not found:
            continue
        p = pivot
        if len(p) == 1:
            pr, pc = p[0]
            mode = 'rot'
        else:
            rs = [r for r,_ in p]
            cs = [c for _,c in p]
            rmin, rmax = min(rs), max(rs)
            cmin, cmax = min(cs), max(cs)
            if rmin == rmax:
                pr = rmin
                mode = 'vert'
            else:
                pc = cmin
                mode = 'horiz'
        for r, c in comp:
            if mode == 'rot':
                nr, nc = 2*pr - r, 2*pc - c
            elif mode == 'vert':
                nr, nc = 2*pr - r, c
            else:
                nr, nc = r, 2*pc - c
            if 0 <= nr < h and 0 <= nc < w and out[nr][nc] == bg:
                out[nr][nc] = color
        processed.add(idx)
    return out