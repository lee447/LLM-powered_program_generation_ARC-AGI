def solve(grid):
    R, C = len(grid), len(grid[0])
    visited = [[False] * C for _ in range(R)]
    comps = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] != 0 and not visited[r][c]:
                val = grid[r][c]
                stack = [(r, c)]
                visited[r][c] = True
                pts = []
                while stack:
                    pr, pc = stack.pop()
                    pts.append((pr, pc))
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = pr + dr, pc + dc
                        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and grid[nr][nc] == val:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                comps.append((pts, val))
    comps.sort(key=lambda x: len(x[0]))
    cluster_pts, cluster_val = comps[0]
    lines = comps[1:]
    frames = sorted([(len(pts), val) for pts, val in lines], key=lambda x: -x[0])
    size = frames[0][0]
    out = [[0] * size for _ in range(size)]
    for depth, (length, color) in enumerate(frames):
        s, e = depth, depth + length - 1
        for i in range(s, e + 1):
            out[s][i] = color
            out[e][i] = color
            out[i][s] = color
            out[i][e] = color
    rows = [r for r, _ in cluster_pts]
    cols = [c for _, c in cluster_pts]
    h = max(rows) - min(rows) + 1
    w = max(cols) - min(cols) + 1
    cs = h if h > w else w
    start = (size - cs) // 2
    for i in range(cs):
        for j in range(cs):
            out[start + i][start + j] = cluster_val
    return out