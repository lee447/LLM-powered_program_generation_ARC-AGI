def solve(grid):
    h = len(grid)
    w = len(grid[0])
    barrier = None
    for c in range(w):
        s = {grid[r][c] for r in range(h)}
        if len(s) == 1 and next(iter(s)) != 0:
            barrier = c
            break
    left_counts = {}
    for r in range(h):
        for c in range(barrier):
            v = grid[r][c]
            if v != 0:
                left_counts[v] = left_counts.get(v, 0) + 1
    left_color = max(left_counts, key=left_counts.get) if left_counts else None
    right_counts = {}
    for r in range(h):
        for c in range(barrier + 1, w):
            v = grid[r][c]
            if v != 0:
                right_counts[v] = right_counts.get(v, 0) + 1
    right_color = max(right_counts, key=right_counts.get) if right_counts else None
    m = min(barrier, w - barrier - 1)
    result = []
    for r in range(h):
        row = [0] * m
        for j in range(m):
            a = grid[r][j] == left_color
            b = grid[r][barrier + 1 + j] == right_color
            if a ^ b:
                row[j] = 2
        result.append(row)
    return result