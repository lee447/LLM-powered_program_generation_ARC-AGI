def solve(grid):
    h = len(grid)
    w = len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    frames = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 3 and not seen[i][j]:
                stack = [(i,j)]
                seen[i][j] = True
                comp = []
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr,nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not seen[nr][nc] and grid[nr][nc] == 3:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                rs = [r for r,c in comp]
                cs = [c for r,c in comp]
                r0,r1 = min(rs), max(rs)
                c0,c1 = min(cs), max(cs)
                center = ((r0+r1)//2, (c0+c1)//2)
                frames.append((r0,r1,c0,c1,center))
    # identify bottom frame
    frames.sort(key=lambda x: x[4][0])
    top_frames = frames[:2]
    bottom = frames[2]
    # among top two, left and right
    top_frames.sort(key=lambda x: x[4][1])
    left, right = top_frames
    out = [row[:] for row in grid]
    # fill right with 1
    cr, cc = right[4]
    for dr in (-1,0,1):
        for dc in (-1,0,1):
            out[cr+dr][cc+dc] = 1
    # fill bottom with 8
    cr, cc = bottom[4]
    for dr in (-1,0,1):
        for dc in (-1,0,1):
            out[cr+dr][cc+dc] = 8
    return out