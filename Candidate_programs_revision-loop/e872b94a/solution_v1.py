def solve(grid):
    m, n = len(grid), len(grid[0])
    pts = [(r, c) for r in range(m) for c in range(n) if grid[r][c] != 0]
    if not pts:
        return []
    shape_color = grid[pts[0][0]][pts[0][1]]
    cnt = 0
    cent_r = sum(r for r, c in pts) / len(pts)
    cent_c = sum(c for r, c in pts) / len(pts)
    ends = []
    for r, c in pts:
        neigh = 0
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            rr, cc = r+dr, c+dc
            if 0 <= rr < m and 0 <= cc < n and grid[rr][cc] == shape_color:
                neigh += 1
        if neigh == 1:
            ends.append((r, c))
    dirs = set()
    for r, c in ends:
        dr, dc = r - cent_r, c - cent_c
        if abs(dr) > abs(dc):
            dirs.add('S' if dr > 0 else 'N')
        else:
            dirs.add('E' if dc > 0 else 'W')
    k = len(dirs)
    return [[0] for _ in range(k)]