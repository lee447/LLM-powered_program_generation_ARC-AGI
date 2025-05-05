from collections import deque

def solve(grid):
    H, W = len(grid), len(grid[0])
    seen = [[False]*W for _ in range(H)]
    bands = {'solid': [], 'hollow': [], 'other': []}
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not seen[i][j]:
                col = grid[i][j]
                q = deque([(i, j)])
                seen[i][j] = True
                cells = []
                while q:
                    r, c = q.popleft()
                    cells.append((r, c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and not seen[nr][nc] and grid[nr][nc]==col:
                            seen[nr][nc] = True
                            q.append((nr, nc))
                rs = [r for r,c in cells]
                cs = [c for r,c in cells]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                h, w = r1-r0+1, c1-c0+1
                cnt = len(cells)
                if cnt == h*w:
                    typ = 'solid'
                elif h>2 and w>2 and cnt == h*w - (h-2)*(w-2):
                    typ = 'hollow'
                else:
                    typ = 'other'
                bands[typ].append((r0, c0, h, w, col, cells))
    solid = sorted(bands['solid'], key=lambda x: x[1])
    hollow = sorted(bands['hollow'], key=lambda x: x[1])
    other = sorted(bands['other'], key=lambda x: x[1])
    h_top = max((h for _,_,h,_,_,_ in solid), default=0)
    h_mid = max((h for _,_,h,_,_,_ in hollow), default=0)
    h_bot = max((h for _,_,h,_,_,_ in other), default=0)
    off_top = 0
    off_mid = off_top + h_top
    off_bot = H - h_bot
    out = [[0]*W for _ in range(H)]
    for grp, off in ((solid, off_top), (hollow, off_mid), (other, off_bot)):
        for r0, c0, h, w, col, cells in grp:
            for r, c in cells:
                out[r-r0+off][c] = col
    return out