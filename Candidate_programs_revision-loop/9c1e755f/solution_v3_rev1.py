from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    out = [row[:] for row in grid]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    comp.append((r,c))
                    for dr, dc in dirs:
                        rr, cc = r+dr, c+dc
                        if 0 <= rr < m and 0 <= cc < n and not visited[rr][cc] and grid[rr][cc] != 0:
                            visited[rr][cc] = True
                            stack.append((rr,cc))
                rs = [r for r,_ in comp]
                cs = [c for _,c in comp]
                minr, maxr = min(rs), max(rs)
                minc, maxc = min(cs), max(cs)
                seeds_H0 = [(r,c,grid[r][c]) for r,c in comp if r==minr or r==maxr]
                seeds_V0 = [(r,c,grid[r][c]) for r,c in comp if c==minc or c==maxc]
                distinct_H0 = {v for _,_,v in seeds_H0}
                distinct_V0 = {v for _,_,v in seeds_V0}
                orientation = None
                if len(distinct_H0) > 1:
                    orientation = 'H'
                elif len(distinct_V0) > 1:
                    orientation = 'V'
                if orientation == 'H':
                    seed_rows = []
                    for r in (minr, maxr):
                        cnt = sum(1 for c in range(minc, maxc+1) if grid[r][c]!=0)
                        if cnt>1:
                            seed_rows.append(r)
                    seed_rows = sorted(seed_rows)
                    D = {}
                    for r in seed_rows:
                        D[r] = {c:grid[r][c] for c in range(minc, maxc+1) if grid[r][c]!=0}
                    k = len(seed_rows)
                    if k > 1:
                        for r in range(minr, maxr+1):
                            idx = (r-minr) % k
                            src = seed_rows[idx]
                            for c,v in D[src].items():
                                out[r][c] = v
                    elif k == 1:
                        seed = seed_rows[0]
                        if seed == maxr:
                            for r in range(minr, maxr+1):
                                for c,v in D[seed].items():
                                    out[r][c] = v
                        else:
                            for r in range(minr, maxr+1):
                                if r == seed: continue
                                v = grid[r][minc]
                                for c in range(minc, maxc+1):
                                    out[r][c] = v
                elif orientation == 'V':
                    seed_cols = []
                    for c in (minc, maxc):
                        cnt = sum(1 for r in range(minr, maxr+1) if grid[r][c]!=0)
                        if cnt>1:
                            seed_cols.append(c)
                    seed_cols = sorted(seed_cols)
                    D2 = {}
                    for c in seed_cols:
                        D2[c] = {r:grid[r][c] for r in range(minr, maxr+1) if grid[r][c]!=0}
                    k = len(seed_cols)
                    if k > 1:
                        for c in range(minc, maxc+1):
                            idx = (c-minc) % k
                            src = seed_cols[idx]
                            for r,v in D2[src].items():
                                out[r][c] = v
                    elif k == 1:
                        seed = seed_cols[0]
                        if seed == maxc:
                            for c in range(minc, maxc+1):
                                for r,v in D2[seed].items():
                                    out[r][c] = v
                        else:
                            for c in range(minc, maxc+1):
                                if c == seed: continue
                                v = grid[minr][c]
                                for r in range(minr, maxr+1):
                                    out[r][c] = v
    return out