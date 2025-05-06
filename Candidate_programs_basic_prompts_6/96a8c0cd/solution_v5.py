def solve(grid):
    from collections import deque
    R, C = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    # find start comp (value 2) and all comps of non-zero cells
    visited = [[False]*C for _ in range(R)]
    comps = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] != 0 and not visited[i][j]:
                color = grid[i][j]
                q = [(i,j)]
                visited[i][j] = True
                comp = [(i,j)]
                for x,y in q:
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<R and 0<=ny<C and not visited[nx][ny] and grid[nx][ny]==color:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                            comp.append((nx,ny))
                comps.append((color, comp))
    # identify start comp and targets
    start = None
    targets = []
    for color, comp in comps:
        if color == 2:
            start = comp[0]
        else:
            # compute neighbor cells
            neigh = set()
            for x,y in comp:
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if 0<=nx<R and 0<=ny<C and grid[nx][ny]==0:
                        neigh.add((nx,ny))
            if neigh:
                # record comp bbox for tie-break
                minr = min(x for x,y in comp)
                minc = min(y for x,y in comp)
                targets.append([minr, minc, neigh])
    cur = start
    # connect comps by BFS nearest-first
    while targets:
        best = None
        best_path = None
        # find comp with shortest BFS
        for idx, (mr, mc, neigh) in enumerate(targets):
            # BFS from cur to any in neigh
            q = deque([cur])
            par = {cur: None}
            found = None
            while q and found is None:
                x,y = q.popleft()
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if 0<=nx<R and 0<=ny<C and (nx,ny) not in par:
                        # allow if free (grid==0) or it's cur or path drawn
                        if (nx,ny)==cur or grid[nx][ny]==0:
                            par[(nx,ny)] = (x,y)
                            if (nx,ny) in neigh:
                                found = (nx,ny)
                                break
                            q.append((nx,ny))
                # end for
            # end BFS
            if found:
                # reconstruct path
                path = []
                p = found
                while p is not None:
                    path.append(p)
                    p = par[p]
                path.reverse()
                dist = len(path)
                if best is None or dist<best[0] or (dist==best[0] and (mr,mc)<(best[1],best[2])):
                    best = (dist, mr, mc, idx)
                    best_path = path
        # draw best path
        _,_,_,bi = best
        path = best_path
        # mark path except first cell
        for x,y in path[1:]:
            out[x][y] = 2
        cur = path[-1]
        # remove target
        targets.pop(bi)
    return out