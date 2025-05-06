def solve(grid):
    from collections import deque
    H, W = len(grid), len(grid[0])
    color = next(c for row in grid for c in row if c != 0)
    seen = [[False]*W for _ in range(H)]
    comps = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(H):
        for j in range(W):
            if grid[i][j]==color and not seen[i][j]:
                q = deque([(i,j)])
                seen[i][j] = True
                comp = []
                while q:
                    r,c = q.popleft()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr,nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and not seen[nr][nc] and grid[nr][nc]==color:
                            seen[nr][nc] = True
                            q.append((nr,nc))
                comps.append(comp)
    offs_list = []
    for comp in comps:
        sr = sum(r for r,c in comp)/len(comp)
        sc = sum(c for r,c in comp)/len(comp)
        sr2 = sr*2
        sc2 = sc*2
        offs = set()
        for r,c in comp:
            offs.add((r*2-int(sr2), c*2-int(sc2)))
        offs_list.append(offs)
    common = set(offs_list[0])
    for offs in offs_list[1:]:
        common &= offs
    if not common:
        common = set().union(*offs_list)
    rs = [r for r,c in common]
    cs = [c for r,c in common]
    minr2, maxr2 = min(rs), max(rs)
    minc2, maxc2 = min(cs), max(cs)
    H2 = (maxr2 - minr2)//2 + 1
    W2 = (maxc2 - minc2)//2 + 1
    out = [[0]*W2 for _ in range(H2)]
    for r2,c2 in common:
        rr = (r2 - minr2)//2
        cc = (c2 - minc2)//2
        if 0 <= rr < H2 and 0 <= cc < W2:
            out[rr][cc] = color
    return out