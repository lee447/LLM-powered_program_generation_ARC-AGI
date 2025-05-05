def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    centers = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 0 and not visited[r][c]:
                v = grid[r][c]
                seg = [(r,c)]
                visited[r][c] = True
                if c+1<w and grid[r][c+1]==v:
                    for dc in (1,2):
                        visited[r][c+dc] = True
                        seg.append((r,c+dc))
                    centers.append((r, c+1))
                elif r+1<h and grid[r+1][c]==v:
                    for dr in (1,2):
                        visited[r+dr][c] = True
                        seg.append((r+dr,c))
                    centers.append((r+1, c))
    out = [row[:] for row in grid]
    byrow = {}
    for r,c in centers:
        byrow.setdefault(r, []).append(c)
    for r, cols in byrow.items():
        cols.sort()
        for i in range(len(cols)-1):
            c1, c2 = cols[i], cols[i+1]
            mid = (c1 + c2)//2
            for d in (-1,0,1):
                x = mid + d
                if 0<=x<w and out[r][x]==0:
                    out[r][x] = 2
    bycol = {}
    for r,c in centers:
        bycol.setdefault(c, []).append(r)
    for c, rows in bycol.items():
        rows.sort()
        for i in range(len(rows)-1):
            r1, r2 = rows[i], rows[i+1]
            mid = (r1 + r2)//2
            for d in (-1,0,1):
                y = mid + d
                if 0<=y<h and out[y][c]==0:
                    out[y][c] = 2
    return out