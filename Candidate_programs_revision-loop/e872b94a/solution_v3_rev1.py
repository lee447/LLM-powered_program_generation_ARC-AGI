def solve(grid):
    m, n = len(grid), len(grid[0])
    pts = [(r, c) for r in range(m) for c in range(n) if grid[r][c] != 0]
    if not pts:
        return []
    color = grid[pts[0][0]][pts[0][1]]
    ends = []
    for r, c in pts:
        neigh = 0
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            rr, cc = r+dr, c+dc
            if 0 <= rr < m and 0 <= cc < n and grid[rr][cc] == color:
                neigh += 1
        if neigh == 1:
            ends.append((r, c))
    k = len(ends)
    return [[0] for _ in range(k)]