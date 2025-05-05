def solve(grid):
    n = len(grid)
    m = len(grid[0])
    rows = {0, n}
    cols = {0, m}
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 4:
                rows.add(r)
                cols.add(c)
    row_anchors = sorted(rows)
    col_anchors = sorted(cols)
    best = []
    best_count = -1
    for i in range(len(row_anchors) - 1):
        r0 = row_anchors[i]
        r1 = row_anchors[i + 1]
        for j in range(len(col_anchors) - 1):
            c0 = col_anchors[j]
            c1 = col_anchors[j + 1]
            temp = []
            count = 0
            for r in range(r0, r1):
                for c in range(c0, c1):
                    if grid[r][c] == 2:
                        temp.append((r - r0, c - c0))
                        count += 1
            if count > best_count:
                best_count = count
                best = temp
    out = [row[:] for row in grid]
    for i in range(len(row_anchors) - 1):
        r0 = row_anchors[i]
        for j in range(len(col_anchors) - 1):
            c0 = col_anchors[j]
            for dr, dc in best:
                r = r0 + dr
                c = c0 + dc
                if 0 <= r < n and 0 <= c < m and grid[r][c] != 4:
                    out[r][c] = 2
    return out