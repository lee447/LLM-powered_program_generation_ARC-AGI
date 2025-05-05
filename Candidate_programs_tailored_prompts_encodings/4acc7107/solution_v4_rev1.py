def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*W for _ in range(H)]
    patches = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v and not seen[r][c]:
                stack = [(r,c)]
                seen[r][c] = True
                cells = []
                min_r = max_r = r
                min_c = max_c = c
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    if x<min_r: min_r = x
                    if x>max_r: max_r = x
                    if y<min_c: min_c = y
                    if y>max_c: max_c = y
                    for dr,dc in dirs:
                        nx,ny = x+dr, y+dc
                        if 0<=nx<H and 0<=ny<W and not seen[nx][ny] and grid[nx][ny]==v:
                            seen[nx][ny] = True
                            stack.append((nx,ny))
                patches.setdefault(v, []).append((min_r, min_c, max_r, max_c, cells))
    order = sorted(patches.keys(), key=lambda col: min(p[1] for p in patches[col]))
    out = [[0]*W for _ in range(H)]
    mid = H//2
    cur_c = 0
    for col in order:
        group = patches[col]
        group.sort(key=lambda p: p[0])
        widths = [p[3]-p[1]+1 for p in group]
        max_w = max(widths)
        r0 = mid
        for min_r, min_c, max_r, max_c, cells in group:
            for x,y in cells:
                out[r0 + (x-min_r)][cur_c + (y-min_c)] = col
            r0 += (max_r-min_r+1) + 1
        cur_c += max_w + 1
    return out