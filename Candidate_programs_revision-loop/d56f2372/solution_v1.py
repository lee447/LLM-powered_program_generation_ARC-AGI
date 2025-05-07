def solve(grid):
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def flood(sr, sc, color):
        stack = [(sr, sc)]
        pts = []
        seen[sr][sc] = True
        while stack:
            r, c = stack.pop()
            pts.append((r, c))
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < h and 0 <= nc < w and not seen[nr][nc] and grid[nr][nc] == color:
                    seen[nr][nc] = True
                    stack.append((nr, nc))
        return pts
    def is_horiz_sym(sub):
        hh = len(sub)
        for i in range(hh//2):
            if sub[i] != sub[hh-1-i]:
                return False
        return True
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                color = grid[i][j]
                pts = flood(i, j, color)
                rs = [p[0] for p in pts]
                cs = [p[1] for p in pts]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                sub = [[0]*(c1-c0+1) for _ in range(r1-r0+1)]
                for r, c in pts:
                    sub[r-r0][c-c0] = color
                if not is_horiz_sym(sub):
                    return sub
    return []