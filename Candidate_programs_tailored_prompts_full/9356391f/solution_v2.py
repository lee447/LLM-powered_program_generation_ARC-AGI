def solve(grid):
    R = len(grid)
    C = len(grid[0])
    runs = []
    in_run = False
    for c in range(C):
        if grid[0][c] != 0:
            if not in_run:
                in_run = True
                start = c
        else:
            if in_run:
                in_run = False
                runs.append((start, c - 1))
    if in_run:
        runs.append((start, C - 1))
    run = max(runs, key=lambda x: x[1] - x[0] + 1)
    start, end = run
    palette = [grid[0][c] for c in range(start, end + 1)]
    stray = None
    for c in range(C):
        if grid[0][c] != 0 and not (start <= c <= end):
            stray = grid[0][c]
            break
    out = [[0] * C for _ in range(R)]
    for c in range(C):
        if start <= c <= end:
            out[0][c] = grid[0][c]
        elif grid[0][c] != 0:
            out[0][c] = 5
    for c in range(C):
        out[1][c] = grid[1][c]
    center_r = center_c = None
    for r in range(2, R):
        for c in range(C):
            if grid[r][c] != 0:
                center_r, center_c = r, c
                break
        if center_r is not None:
            break
    for i, color in enumerate(palette):
        for dr in range(-i, i + 1):
            for dc in range(-i, i + 1):
                if max(abs(dr), abs(dc)) == i:
                    rr = center_r + dr
                    cc = center_c + dc
                    if 0 <= rr < R and 0 <= cc < C:
                        out[rr][cc] = color
    if stray is not None:
        radius = (center_r - 1) // 2
        i = radius
        for dr in range(-i, i + 1):
            for dc in range(-i, i + 1):
                if max(abs(dr), abs(dc)) == i:
                    rr = center_r + dr
                    cc = center_c + dc
                    if 0 <= rr < R and 0 <= cc < C:
                        out[rr][cc] = stray
    return out