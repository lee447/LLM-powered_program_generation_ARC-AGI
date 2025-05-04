def solve(grid):
    orig_header = grid[0][:]
    m = len(orig_header)
    ring_color = {j: orig_header[j] for j in range(m) if orig_header[j] != 0}
    center_color = ring_color.get(0)
    ci = cj = None
    for i in range(2, len(grid)):
        for j in range(m):
            if grid[i][j] == center_color:
                ci, cj = i, j
                break
        if ci is not None:
            break
    if ci is None:
        return grid
    max_ring = max(ring_color.keys())
    for i in range(len(grid)):
        for j in range(m):
            d = max(abs(i - ci), abs(j - cj))
            if d in ring_color:
                grid[i][j] = ring_color[d]
    # clean header beyond contiguous prefix
    prefix = 0
    while prefix < m and orig_header[prefix] != 0:
        prefix += 1
    for j in range(prefix, m):
        if orig_header[j] != 0:
            grid[0][j] = grid[1][j]
    return grid