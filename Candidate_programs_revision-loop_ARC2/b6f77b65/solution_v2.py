def solve(grid):
    h, w = len(grid), len(grid[0])
    C = grid[0][0]
    blocks = [(2, 5, 3), (5, 8, 3), (8, h, h-8)]
    idx = None
    for i, (r0, r1, _) in enumerate(blocks):
        for r in range(r0, r1):
            if C in grid[r]:
                idx = i
                break
        if idx is not None:
            break
    if idx is None:
        return grid
    new = [[0]*w for _ in range(h)]
    new[0][0] = C
    for c in range(1, w):
        new[0][c] = grid[0][c]
    for r in range(1, h):
        new[r][0] = grid[r][0]
    for i, (r0, r1, sz) in enumerate(blocks):
        src = blocks[(i+1)%3]
        for r in range(r0, r1):
            for c in range(1, w):
                new[r][c] = grid[r - r0 + src[0]][c] if src[0] <= r - r0 + src[0] < src[1] else 0
    return new