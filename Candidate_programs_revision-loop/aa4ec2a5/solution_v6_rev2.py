import collections

def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs4 = [(-1,0),(1,0),(0,-1),(0,1)]
    seen = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not seen[i][j]:
                comp = []
                dq = collections.deque([(i,j)])
                seen[i][j] = True
                while dq:
                    r,c = dq.popleft()
                    comp.append((r,c))
                    for dr,dc in dirs4:
                        rr,cc = r+dr, c+dc
                        if 0<=rr<h and 0<=cc<w and grid[rr][cc]==1 and not seen[rr][cc]:
                            seen[rr][cc] = True
                            dq.append((rr,cc))
                clusters.append(comp)
    clusters.sort(key=len, reverse=True)
    out = [[4]*w for _ in range(h)]
    color_map = {1:2,2:8,3:6}
    for comp in clusters[:2]:
        dist = {}
        dq = collections.deque()
        for r,c in comp:
            dist[(r,c)] = 0
            dq.append((r,c,0))
        while dq:
            r,c,d = dq.popleft()
            if d == 3: continue
            for dr,dc in dirs4:
                rr,cc = r+dr, c+dc
                if 0<=rr<h and 0<=cc<w and (rr,cc) not in dist and grid[rr][cc]!=1:
                    dist[(rr,cc)] = d+1
                    dq.append((rr,cc,d+1))
        for (r,c),d in dist.items():
            if d in color_map:
                out[r][c] = color_map[d]
        for r,c in comp:
            out[r][c] = 1
    return out