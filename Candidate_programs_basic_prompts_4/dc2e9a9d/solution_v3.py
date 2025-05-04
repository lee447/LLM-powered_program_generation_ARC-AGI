def solve(grid):
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 3 and not seen[i][j]:
                stack = [(i,j)]
                seen[i][j] = True
                cells = []
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not seen[nr][nc] and grid[nr][nc] == 3:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                rs = [r for r,c in cells]
                cs = [c for r,c in cells]
                r0,r1,c0,c1 = min(rs), max(rs), min(cs), max(cs)
                shapes.append((r0,c0,r1,c1,cells))
    shapes.sort(key=lambda x:(x[0],x[1]))
    out = [row[:] for row in grid]
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    for idx, (r0,c0,r1,c1,cells) in enumerate(shapes):
        dr,dc = dirs[idx%4]
        ph = r1-r0+1
        pw = c1-c0+1
        sr = r0 + dr*(ph+1) if dr else r0
        sc = c0 + dc*(pw+1) if dc else c0
        color = 1 if idx%2==0 else 8
        for r,c in cells:
            nr = r - r0 + sr
            nc = c - c0 + sc
            if 0 <= nr < h and 0 <= nc < w:
                out[nr][nc] = color
    return out