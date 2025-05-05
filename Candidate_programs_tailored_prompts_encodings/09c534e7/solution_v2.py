from collections import deque
def solve(grid):
    m, n = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited = [[False]*n for _ in range(m)]
    clusters = []
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1 and not visited[r][c]:
                q = deque([(r,c)])
                pix = []
                visited[r][c] = True
                while q:
                    x,y = q.popleft()
                    pix.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                rs = [p[0] for p in pix]; cs = [p[1] for p in pix]
                r0, r1 = min(rs), max(rs); c0, c1 = min(cs), max(cs)
                sig = frozenset((x-r0, y-c0) for x,y in pix)
                clusters.append({'pix':set(pix),'r0':r0,'r1':r1,'c0':c0,'c1':c1,'sig':sig})
    shape_groups = {}
    for i,cl in enumerate(clusters):
        shape_groups.setdefault(cl['sig'], []).append(i)
    seed_info = {}
    for sig, ids in shape_groups.items():
        found = False
        for i in ids:
            cl = clusters[i]
            for rr in range(cl['r0'], cl['r1']+1):
                for cc in range(cl['c0'], cl['c1']+1):
                    v = grid[rr][cc]
                    if v != 0 and v != 1:
                        sr, sc, color = rr, cc, v
                        found = True
                        break
                if found: break
            if found:
                vis = set()
                q = deque([(sr,sc)])
                while q:
                    x,y = q.popleft()
                    if (x,y) in vis: continue
                    if grid[x][y] == 1: continue
                    if not (cl['r0'] <= x <= cl['r1'] and cl['c0'] <= y <= cl['c1']): continue
                    vis.add((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if (nx,ny) not in vis:
                            q.append((nx,ny))
                rel = set((x-cl['r0'], y-cl['c0']) for x,y in vis)
                seed_info[sig] = (rel, color)
                break
    for sig, (rel, color) in seed_info.items():
        for i in shape_groups[sig]:
            cl = clusters[i]
            for dr,dc in rel:
                out[cl['r0']+dr][cl['c0']+dc] = color
    return out