from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    col = next(c for row in grid for c in row if c != 0)
    seen = [[False] * C for _ in range(R)]
    comps = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == col and not seen[i][j]:
                q = [(i, j)]
                seen[i][j] = True
                pts = []
                for x, y in q:
                    pts.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == col and not seen[nx][ny]:
                            seen[nx][ny] = True
                            q.append((nx, ny))
                rs = [p[0] for p in pts]
                cs = [p[1] for p in pts]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                sub = [row[c0:c1+1] for row in grid[r0:r1+1]]
                comps.append((r1-r0+1, c1-c0+1, sub))
    if not comps:
        return grid
    min_h = min(h for h, w, _ in comps)
    min_w = min(w for h, w, _ in comps)
    trimmed = []
    for h, w, sub in comps:
        ro = (h - min_h) // 2
        co = (w - min_w) // 2
        trimmed.append([row[co:co+min_w] for row in sub[ro:ro+min_h]])
    res = [[col if all(trimmed[k][i][j] == col for k in range(len(trimmed))) else 0
            for j in range(min_w)] for i in range(min_h)]
    return res