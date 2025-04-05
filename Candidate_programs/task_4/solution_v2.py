def solve(grid):
    rows, cols = len(grid), len(grid[0])
    blues = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 1]
    if len(blues) < 2:
        return grid
    blues.sort()
    dr = blues[1][0] - blues[0][0]
    dc = blues[1][1] - blues[0][1]
    chain = [blues[0]]
    for pos in blues[1:]:
        pr, pc = chain[-1]
        if (pos[0] - pr, pos[1] - pc) == (dr, dc):
            chain.append(pos)
    r, c = chain[-1]
    while True:
        r, c = r + dr, c + dc
        if not (0 <= r < rows and 0 <= c < cols):
            break
        if grid[r][c] == 1:
            continue
        grid[r][c] = 2
    return grid