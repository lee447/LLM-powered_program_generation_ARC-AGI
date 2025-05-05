def solve(grid):
    h = len(grid)
    w = len(grid[0])
    c = next(col for row in grid for col in row if col != 0)
    visited = [[False] * w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == c and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                cells = []
                minr = i; maxr = i; minc = j; maxc = j
                while stack:
                    x, y = stack.pop()
                    cells.append((x, y))
                    if x < minr: minr = x
                    if x > maxr: maxr = x
                    if y < minc: minc = y
                    if y > maxc: maxc = y
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == c:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                clusters.append((minr, minc, maxr, maxc, cells))
    midr, midc = h // 2, w // 2
    cand = [cl for cl in clusters if cl[0] >= midr and cl[1] <= midc]
    if not cand:
        cand = clusters
    minr, minc, maxr, maxc, cells = max(cand, key=lambda cl: len(cl[4]))
    H = maxr - minr + 1
    W = maxc - minc + 1
    mask = [[0] * W for _ in range(H)]
    for x, y in cells:
        mask[x - minr][y - minc] = 1
    # Zhang-Suen thinning
    changed = True
    while changed:
        changed = False
        for step in (1, 2):
            to_remove = []
            for i in range(1, H-1):
                for j in range(1, W-1):
                    if mask[i][j] != 1: continue
                    P2 = mask[i-1][j]; P3 = mask[i-1][j+1]; P4 = mask[i][j+1]
                    P5 = mask[i+1][j+1]; P6 = mask[i+1][j]; P7 = mask[i+1][j-1]
                    P8 = mask[i][j-1]; P9 = mask[i-1][j-1]
                    B = P2+P3+P4+P5+P6+P7+P8+P9
                    if B < 2 or B > 6: continue
                    A = (P2==0 and P3==1) + (P3==0 and P4==1) + (P4==0 and P5==1) + (P5==0 and P6==1) + (P6==0 and P7==1) + (P7==0 and P8==1) + (P8==0 and P9==1) + (P9==0 and P2==1)
                    if A != 1: continue
                    if step == 1:
                        if P2 * P4 * P6 != 0: continue
                        if P4 * P6 * P8 != 0: continue
                    else:
                        if P2 * P4 * P8 != 0: continue
                        if P2 * P6 * P8 != 0: continue
                    to_remove.append((i, j))
            if to_remove:
                changed = True
                for i, j in to_remove:
                    mask[i][j] = 0
    out = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if mask[i][j]:
                out[i][j] = c
    return out