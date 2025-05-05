def solve(grid):
    from collections import deque
    H, W = len(grid), len(grid[0])
    seen = [[False]*W for _ in range(H)]
    clusters = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not seen[i][j]:
                col = grid[i][j]
                q = deque([(i,j)])
                seen[i][j] = True
                cells = []
                while q:
                    r,c = q.popleft()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and not seen[nr][nc] and grid[nr][nc]==col:
                            seen[nr][nc] = True
                            q.append((nr,nc))
                rs = [r for r,c in cells]
                cs = [c for r,c in cells]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                h, w = r1-r0+1, c1-c0+1
                cnt = len(cells)
                if h==w and cnt==h*w:
                    typ = 'solid'
                elif h==w and cnt==h*w-1:
                    typ = 'hollow'
                elif (h==1 or w==1) and cnt>1:
                    typ = 'other'
                else:
                    # plus or irregular => other
                    typ = 'other'
                clusters.append((typ, r0, c0, h, w, grid[r0][c0], cells))
    bands = {'hollow':[], 'solid':[], 'other':[]}
    for cl in clusters:
        bands[cl[0]].append(cl)
    top = sorted(bands['hollow'], key=lambda x: x[2])
    mid = sorted(bands['solid'], key=lambda x: x[2])
    bot = sorted(bands['other'], key=lambda x: x[2])
    h_top = max((c[3] for c in top), default=0)
    h_mid = max((c[3] for c in mid), default=0)
    h_bot = max((c[3] for c in bot), default=0)
    off_top = 0
    off_mid = off_top + h_top
    off_bot = H - h_bot
    out = [[0]*W for _ in range(H)]
    for grp,off in ((top,off_top),(mid,off_mid),(bot,off_bot)):
        for _, r0, c0, h, w, col, cells in grp:
            for r,c in cells:
                out[r - r0 + off][c] = col
    return out