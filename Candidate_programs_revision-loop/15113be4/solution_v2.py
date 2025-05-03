def solve(grid):
    H, W = len(grid), len(grid[0])
    bands = []
    divs = [-1] + [r for r in range(H) if all(grid[r][c] == 4 for c in range(W))] + [H]
    for i in range(len(divs)-1):
        a, b = divs[i]+1, divs[i+1]
        if a < b:
            bands.append((a, b))
    for r0, r1 in bands:
        seed = []
        color = None
        for i in range(r0, r1):
            for j in range(W):
                v = grid[i][j]
                if v not in (0,1,4):
                    seed.append((i,j))
                    color = v
        if not seed:
            continue
        sy = sum(i for i,_ in seed)/len(seed)
        sx = sum(j for _,j in seed)/len(seed)
        seen = [[False]*W for _ in range(H)]
        for i in range(r0, r1):
            for j in range(W):
                if grid[i][j] == 1 and not seen[i][j]:
                    comp = []
                    stack = [(i,j)]
                    seen[i][j] = True
                    while stack:
                        y,x = stack.pop()
                        comp.append((y,x))
                        for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                            ny, nx = y+dy, x+dx
                            if r0 <= ny < r1 and 0 <= nx < W and grid[ny][nx] == 1 and not seen[ny][nx]:
                                seen[ny][nx] = True
                                stack.append((ny,nx))
                    cy = sum(y for y,_ in comp)/len(comp)
                    cx = sum(x for _,x in comp)/len(comp)
                    dy = cy - sy
                    dx = cx - sx
                    for (sy_i, sx_i) in seed:
                        ty = sy_i + dy
                        tx = sx_i + dx
                        yi = int(round(ty))
                        xi = int(round(tx))
                        if r0 <= yi < r1 and 0 <= xi < W and grid[yi][xi] == 1:
                            grid[yi][xi] = color
    return grid