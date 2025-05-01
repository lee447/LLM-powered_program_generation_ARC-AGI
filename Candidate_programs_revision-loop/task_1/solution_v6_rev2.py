def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    patterns = {}
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                while stack:
                    r, c = stack.pop()
                    cells.append((r, c))
                    for dr, dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                if len(cells) < 2:
                    continue
                rs = [r for r,_ in cells]
                cs = [c for _,c in cells]
                r0, c0 = min(rs), min(cs)
                r1, c1 = max(rs), max(cs)
                hh, ww = r1-r0+1, c1-c0+1
                if len(cells) != hh*ww:
                    continue
                pat = tuple(sorted((r-r0, c-c0, grid[r][c]) for r,c in cells))
                key = (hh, ww, pat)
                patterns.setdefault(key, []).append((r0, c0))
    out = [[0]*w for _ in range(h)]
    for (_, _, pat), origins in patterns.items():
        if len(origins) >= 2:
            for r0, c0 in origins:
                for dr, dc, v in pat:
                    out[r0+dr][c0+dc] = v
    return out