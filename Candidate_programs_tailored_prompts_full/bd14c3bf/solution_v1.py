def solve(grid):
    h, w = len(grid), len(grid[0])
    twos = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    ar = min(r for r,_ in twos)
    ac_min = min(c for r,c in twos if r == ar)
    ac_max = max(c for r,c in twos if r == ar)
    ac = min(c for r,c in twos)
    ar_min = min(r for r,c in twos if c == ac)
    ar_max = max(r for r,c in twos if c == ac)
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not seen[i][j]:
                stack = [(i,j)]
                cluster = []
                seen[i][j] = True
                while stack:
                    r,c = stack.pop()
                    cluster.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not seen[nr][nc] and grid[nr][nc] == 1:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                rs = [r for r,_ in cluster]
                cs = [c for _,c in cluster]
                mn_r, mx_r = min(rs), max(rs)
                mn_c, mx_c = min(cs), max(cs)
                under_h = mn_r > ar and any(ac_min <= c <= ac_max for _,c in cluster)
                under_v = mn_c > ac and any(ar_min <= r <= ar_max for r,_ in cluster)
                if under_h or under_v:
                    for r,c in cluster:
                        grid[r][c] = 2
    return grid