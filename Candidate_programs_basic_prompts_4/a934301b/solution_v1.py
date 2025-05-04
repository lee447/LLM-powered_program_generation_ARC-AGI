def solve(grid):
    m = len(grid)
    n = len(grid[0])
    visited = [[False]*n for _ in range(m)]
    comps = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i, j)]
                comp = []
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr, cc = r+dr, c+dc
                        if 0 <= rr < m and 0 <= cc < n and grid[rr][cc] != 0 and not visited[rr][cc]:
                            visited[rr][cc] = True
                            stack.append((rr, cc))
                rs = [r for r,_ in comp]
                cs = [c for _,c in comp]
                r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
                area = (r1-r0+1)*(c1-c0+1)
                if area == len(comp):
                    cnt8 = sum(1 for r,c in comp if grid[r][c] == 8)
                    if cnt8 <= 1:
                        comps.append((r0, c0, comp))
    keep = set()
    for _, _, comp in comps[:3]:
        for cell in comp:
            keep.add(cell)
    out = [[0]*n for _ in range(m)]
    for r,c in keep:
        out[r][c] = grid[r][c]
    return out