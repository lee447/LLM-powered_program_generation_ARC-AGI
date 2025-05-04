from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*m for _ in range(n)]
    bars = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 5 and not seen[i][j]:
                stack = [(i,j)]
                seen[i][j] = True
                comp = []
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < m and not seen[nx][ny] and grid[nx][ny] == 5:
                            seen[nx][ny] = True
                            stack.append((nx,ny))
                bars.append(comp)
    for bar in bars:
        rs = [r for r,c in bar]; cs = [c for r,c in bar]
        rmin, rmax, cmin, cmax = min(rs), max(rs), min(cs), max(cs)
        orient = 'v' if cmin==cmax else 'h'
        strip = set()
        for r,c in bar:
            for dr,dc in dirs:
                rr, cc = r+dr, c+dc
                if 0 <= rr < n and 0 <= cc < m and grid[rr][cc] not in (0,5):
                    strip.add((rr,cc))
        if not strip:
            continue
        srmin = min(r for r,c in strip); srmax = max(r for r,c in strip)
        scmin = min(c for r,c in strip); scmax = max(c for r,c in strip)
        ph = srmax - srmin + 1; pw = scmax - scmin + 1
        pat = [grid[r][scmin:scmax+1] for r in range(srmin, srmax+1)]
        if orient == 'v':
            if scmin > cmax:
                col_start, col_end = cmax+1, m-2
            else:
                col_start, col_end = 1, cmin-1
            row_start, row_end = rmin, rmax
        else:
            if srmin > rmax:
                row_start, row_end = 1, rmin-1
            else:
                row_start, row_end = rmax+1, n-2
            col_start, col_end = cmin, cmax
        if row_start <= row_end and col_start <= col_end:
            for i in range(row_start, row_end+1):
                for j in range(col_start, col_end+1):
                    res[i][j] = pat[(i-row_start) % ph][(j-col_start) % pw]
    return res