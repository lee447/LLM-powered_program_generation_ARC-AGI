def solve(grid):
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not visited[i][j]:
                comp = []
                stack = [(i,j)]
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and grid[nr][nc] != 0:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                comps.append(comp)
    main = max(comps, key=len)
    main_set = set(main)
    stray = [(r,c) for r in range(H) for c in range(W) if grid[r][c]==5 and (r,c) not in main_set]
    main5 = [(r,c) for (r,c) in main if grid[r][c]==5]
    drdc = None
    for sr, sc in stray:
        for r, c in main5:
            dr, dc = sr-r, sc-c
            ok = True
            for pr, pc in main:
                tr, tc = pr+dr, pc+dc
                if not (0 <= tr < H and 0 <= tc < W):
                    ok = False; break
                if grid[tr][tc] != 0 and grid[pr][pc] != 5:
                    ok = False; break
            if ok:
                drdc = (dr, dc)
                break
        if drdc:
            break
    out = [row[:] for row in grid]
    for r, c in stray:
        out[r][c] = 0
    if drdc:
        dr, dc = drdc
        for pr, pc in main:
            v = grid[pr][pc]
            if v != 5:
                out[pr+dr][pc+dc] = v
    return out