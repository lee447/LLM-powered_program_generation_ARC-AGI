from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for c in row:
            counts[c] = counts.get(c, 0) + 1
    floor = max(counts, key=lambda c: counts[c])
    others = [c for c in counts if c != floor]
    wall = max(others, key=lambda c: counts[c])
    blocks = [c for c in others if c != wall]
    dq = deque()
    ext = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in (0, w-1):
            if grid[i][j] != wall and not ext[i][j]:
                ext[i][j] = True
                dq.append((i,j))
    for j in range(w):
        for i in (0, h-1):
            if grid[i][j] != wall and not ext[i][j]:
                ext[i][j] = True
                dq.append((i,j))
    while dq:
        i,j = dq.popleft()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < h and 0 <= nj < w and not ext[ni][nj] and grid[ni][nj] != wall:
                ext[ni][nj] = True
                dq.append((ni,nj))
    seen = [[False]*w for _ in range(h)]
    comps = []
    comp_block = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != wall and not ext[i][j] and not seen[i][j]:
                dq = deque([(i,j)])
                seen[i][j] = True
                cells = [(i,j)]
                bcol = None
                if grid[i][j] in blocks:
                    bcol = grid[i][j]
                while dq:
                    x,y = dq.popleft()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and grid[nx][ny] != wall and not ext[nx][ny]:
                            seen[nx][ny] = True
                            dq.append((nx,ny))
                            cells.append((nx,ny))
                            if grid[nx][ny] in blocks:
                                bcol = grid[nx][ny]
                comps.append(cells)
                comp_block.append(bcol)
    asc = sorted(blocks, key=lambda c: counts[c])
    small, mid = asc[0], asc[1]
    out = [row[:] for row in grid]
    for cells, b in zip(comps, comp_block):
        if b is None: continue
        fill = 5 if b == small else 3
        for i,j in cells:
            out[i][j] = fill
    return out