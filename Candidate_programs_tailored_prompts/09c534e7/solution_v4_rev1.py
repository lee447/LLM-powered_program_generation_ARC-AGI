from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited = [[False]*C for _ in range(R)]
    comps = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                comps.append(comp)
    for comp in comps:
        rs = [r for r,c in comp]
        cs = [c for r,c in comp]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        if r1 - r0 < 2 or c1 - c0 < 2:
            continue
        rows = list(range(r0+1, r1))
        cols = list(range(c0+1, c1))
        anchor = None
        for r in rows:
            for c in cols:
                v = grid[r][c]
                if v not in (0,1):
                    anchor = (r, c, v)
                    break
            if anchor:
                break
        if not anchor:
            continue
        ar, ac, av = anchor
        h, w = len(rows), len(cols)
        if h == 1 or w == 1:
            for r in rows:
                for c in cols:
                    out[r][c] = av
        else:
            s = min(h, w)
            idx_r = rows.index(ar)
            idx_c = cols.index(ac)
            start_r = idx_r - s//2
            start_c = idx_c - s//2
            if start_r < 0:
                start_r = 0
            if start_c < 0:
                start_c = 0
            if start_r + s > h:
                start_r = h - s
            if start_c + s > w:
                start_c = w - s
            rows_sq = rows[start_r:start_r+s]
            cols_sq = cols[start_c:start_c+s]
            sqset = {(r,c) for r in rows_sq for c in cols_sq}
            for r in rows:
                for c in cols:
                    out[r][c] = av if (r,c) in sqset else 1
    return out