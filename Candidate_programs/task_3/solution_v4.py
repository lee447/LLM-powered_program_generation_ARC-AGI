def solve(grid):
    from collections import deque
    R = len(grid)
    C = len(grid[0]) if R else 0
    out = [row[:] for row in grid]
    seen = [[False]*C for _ in range(R)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(R):
        for j in range(C):
            if grid[i][j] != 0 and not seen[i][j]:
                comp = []
                dq = deque()
                dq.append((i,j))
                seen[i][j] = True
                while dq:
                    r,c = dq.popleft()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<R and 0<=nc<C and grid[nr][nc] != 0 and not seen[nr][nc]:
                            seen[nr][nc] = True
                            dq.append((nr,nc))
                # determine target as the maximum original value in the component
                tgt = max(grid[r][c] for r,c in comp)
                # compute distances from border; border if any 4-neighbor is out of comp (or out-of-bound or 0)
                comp_set = set(comp)
                dist = {}
                dq2 = deque()
                for (r,c) in comp:
                    is_border = False
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if not (0<=nr<R and 0<=nc<C) or ((nr,nc) not in comp_set):
                            is_border = True
                            break
                    if is_border:
                        dist[(r,c)] = 0
                        dq2.append((r,c))
                while dq2:
                    r,c = dq2.popleft()
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if (nr,nc) in comp_set and (nr,nc) not in dist:
                            dist[(nr,nc)] = dist[(r,c)] + 1
                            dq2.append((nr,nc))
                if dist:
                    maxd = max(dist.values())
                else:
                    maxd = 0
                for (r,c) in comp:
                    d = dist.get((r,c),0)
                    if maxd == 0:
                        newcol = grid[r][c]
                    else:
                        newcol = 1 if d==0 else 1 + int(round((tgt - 1)* d/ maxd))
                    out[r][c] = newcol
    return out