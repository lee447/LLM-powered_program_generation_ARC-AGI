def solve(grid):
    H, W = len(grid), len(grid[0])
    seen = [[False]*W for _ in range(H)]
    blocks = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 5 and not seen[i][j]:
                stack = [(i,j)]
                seen[i][j] = True
                coords = []
                while stack:
                    r,c = stack.pop()
                    coords.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and not seen[nr][nc] and grid[nr][nc] == 5:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                rs = [r for r,_ in coords]
                cs = [c for _,c in coords]
                blocks.append((min(rs), min(cs), max(rs), max(cs)))
    hs = sorted(set(b[0] for b in blocks))
    ws = sorted(set(b[1] for b in blocks))
    h = blocks[0][2] - blocks[0][0] + 1
    w = blocks[0][3] - blocks[0][1] + 1
    y0, y1, y2 = hs
    x0, x1, x2 = ws
    stripe_rows = []
    for a,b in ((y0,y1),(y1,y2)):
        stripe_rows += list(range(a+h, b))
    stripe_cols = []
    for a,b in ((x0,x1),(x1,x2)):
        stripe_cols += list(range(a+w, b))
    ans = [row[:] for row in grid]
    for r in stripe_rows:
        for c in range(x0, x2+w):
            if ans[r][c] == 0:
                ans[r][c] = 2
        if x0 > 0:
            for c in range(0, x0):
                if ans[r][c] == 0:
                    ans[r][c] = 1
        if x2+w < W:
            for c in range(x2+w, W):
                if ans[r][c] == 0:
                    ans[r][c] = 1
    for c in stripe_cols:
        for r in range(y0, y2+h):
            if ans[r][c] == 0:
                ans[r][c] = 2
        if y0 > 0:
            for r in range(0, y0):
                if ans[r][c] == 0:
                    ans[r][c] = 1
        if y2+h < H:
            for r in range(y2+h, H):
                if ans[r][c] == 0:
                    ans[r][c] = 1
    return ans