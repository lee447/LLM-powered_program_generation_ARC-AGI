def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    greys = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==5]
    src = None
    for r,c in greys:
        for dr,dc in dirs:
            nr,nc = r+dr, c+dc
            if 0<=nr<h and 0<=nc<w and grid[nr][nc] not in (0,5):
                src = (r,c)
                break
        if src: break
    dest = greys[1] if greys[0]==src else greys[0]
    sr,sc = src
    visited = set()
    stack = []
    for dr,dc in dirs:
        nr,nc = sr+dr, sc+dc
        if 0<=nr<h and 0<=nc<w and grid[nr][nc] not in (0,5):
            visited.add((nr,nc))
            stack.append((nr,nc))
    while stack:
        r,c = stack.pop()
        for dr,dc in dirs:
            nr,nc = r+dr, c+dc
            if 0<=nr<h and 0<=nc<w and grid[nr][nc] not in (0,5) and (nr,nc) not in visited:
                visited.add((nr,nc))
                stack.append((nr,nc))
    offsets = [(r-sr, c-sc, grid[r][c]) for r,c in visited]
    out = [row[:] for row in grid]
    dr0, dc0 = dest
    for dr,dc,val in offsets:
        out[dr0+dr][dc0+dc] = val
    return out