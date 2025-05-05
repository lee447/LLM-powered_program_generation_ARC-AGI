def solve(grid):
    H, W = len(grid), len(grid[0])
    orig = [row[:] for row in grid]
    # find clusters of 6
    visited = [[False]*W for _ in range(H)]
    clusters = []
    for i in range(H):
        for j in range(W):
            if orig[i][j]==6 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0<=nr<H and 0<=nc<W and not visited[nr][nc] and orig[nr][nc]==6:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                if len(comp)>1:
                    clusters.append(comp)
    new4 = set()
    # for each cluster place two 2x2 from its two largest (r+c) cells
    for comp in clusters:
        comp_sorted = sorted(comp, key=lambda x: -(x[0]+x[1]))
        for r,c in comp_sorted[:2]:
            if c<=3:  # skip near anchor
                continue
            for dr in (0,1):
                for dc in (0,1):
                    rr,cc = r+dr, c+dc
                    if 0<=rr<H and 0<=cc<W and orig[rr][cc]!=6:
                        new4.add((rr,cc))
    out = [row[:] for row in orig]
    for r,c in new4:
        out[r][c] = 4
    return out