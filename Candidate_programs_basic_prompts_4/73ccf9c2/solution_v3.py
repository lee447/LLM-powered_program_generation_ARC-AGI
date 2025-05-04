def solve(grid):
    from collections import deque
    H, W = len(grid), len(grid[0])
    cnt = {}
    for i in range(H):
        for j in range(W):
            v = grid[i][j]
            if v:
                cnt[v] = cnt.get(v, 0) + 1
    if not cnt:
        return grid
    color = max(cnt, key=cnt.get)
    seen = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == color and not seen[i][j]:
                q = deque([(i,j)])
                seen[i][j] = True
                cells = []
                minr, maxr = i, i
                minc, maxc = j, j
                while q:
                    r, c = q.popleft()
                    cells.append((r,c))
                    minr = min(minr, r)
                    maxr = max(maxr, r)
                    minc = min(minc, c)
                    maxc = max(maxc, c)
                    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<H and 0<=nc<W and not seen[nr][nc] and grid[nr][nc]==color:
                            seen[nr][nc] = True
                            q.append((nr,nc))
                comps.append((len(cells), minr, maxr, minc, maxc, set(cells)))
    comps.sort(key=lambda x: x[0])
    idx = (len(comps)-1)//2
    _, r0, r1, c0, c1, cells = comps[idx]
    out = []
    for r in range(r0, r1+1):
        row = []
        for c in range(c0, c1+1):
            row.append(color if (r,c) in cells else 0)
        out.append(row)
    return out