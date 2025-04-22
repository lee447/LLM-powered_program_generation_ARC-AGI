def solve(grid):
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    comps = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 0 and not visited[r][c]:
                val = grid[r][c]
                coords = [(r, c)]
                visited[r][c] = True
                stack = [(r, c)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == val:
                            visited[nx][ny] = True
                            coords.append((nx, ny))
                            stack.append((nx, ny))
                comps.append((coords, val))
    segments = []
    cluster = None
    for coords, val in comps:
        size = len(coords)
        rows = [r for r, _ in coords]
        cols = [c for _, c in coords]
        row_span = max(rows) - min(rows) + 1
        col_span = max(cols) - min(cols) + 1
        aligned = (row_span == 1 or col_span == 1)
        if aligned and size > 2:
            segments.append((size, val))
        else:
            cluster = (coords, val)
    segments.sort(key=lambda x: -x[0])
    s_out = segments[0][0]
    d = len(segments)
    coords_c, val_c = cluster
    rows_c = [r for r, _ in coords_c]
    cols_c = [c for _, c in coords_c]
    row_span_c = max(rows_c) - min(rows_c) + 1
    col_span_c = max(cols_c) - min(cols_c) + 1
    cluster_size = max(row_span_c, col_span_c)
    out = [[0]*s_out for _ in range(s_out)]
    for i, (_, color) in enumerate(segments):
        for c in range(i, s_out - i):
            out[i][c] = color
            out[s_out - 1 - i][c] = color
        for r in range(i, s_out - i):
            out[r][i] = color
            out[r][s_out - 1 - i] = color
    offset = d
    for r in range(cluster_size):
        for c in range(cluster_size):
            out[offset + r][offset + c] = val_c
    return out