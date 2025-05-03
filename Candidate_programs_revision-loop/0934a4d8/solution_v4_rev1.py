def solve(grid):
    R, C = len(grid), len(grid[0])
    pts = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 8]
    if not pts:
        return grid
    rs = [r for r, c in pts]
    cs = [c for r, c in pts]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    h, w = r1 - r0 + 1, c1 - c0 + 1
    seen = set()
    tiles = []
    for r in range(R - h + 1):
        for c in range(C - w + 1):
            if any(grid[r+i][c+j] == 8 for i in range(h) for j in range(w)):
                continue
            block = tuple(tuple(grid[r+i][c+j] for j in range(w)) for i in range(h))
            if block not in seen:
                seen.add(block)
                tiles.append(block)
    if len(tiles) == 1:
        return [list(row) for row in tiles[0]]
    if len(tiles) <= h:
        return [list(row) for row in tiles]
    return [list(row) for row in tiles[:h]]