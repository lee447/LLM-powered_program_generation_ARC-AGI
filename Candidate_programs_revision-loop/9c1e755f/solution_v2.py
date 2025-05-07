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
                if orientation == 'V':
                    seeds = [(r,c,grid[r][c]) for r,c in comp if c==minc or c==maxc]
                    for r,c,v in seeds:
                        for cc in range(minc, maxc+1):
                            out[r][cc] = v
                elif orientation == 'H':
                    seed_rows_block = []
                    for r in range(maxr, minr-1, -1):
                        cnt = 0
                        for c in range(minc, maxc+1):
                            if grid[r][c] != 0:
                                cnt += 1
                                if cnt >= 2:
                                    break
                        if cnt >= 2:
                            seed_rows_block.append(r)
                        else:
                            break
                    seed_rows = sorted(seed_rows_block)
                    D = {}
                    for r in seed_rows:
                        D[r] = {}
                        for c in range(minc, maxc+1):
                            if grid[r][c] != 0:
                                D[r][c] = grid[r][c]
                    L = len(seed_rows)
                    for r in range(minr, maxr+1):
                        idx = (r - minr) % L
                        src = seed_rows[idx]
                        for c, v in D[src].items():
                            out[r][c] = v
    return out