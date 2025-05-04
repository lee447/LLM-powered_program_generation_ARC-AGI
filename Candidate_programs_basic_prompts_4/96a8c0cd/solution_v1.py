def solve(grid):
    h = len(grid)
    w = len(grid[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    # find clusters: connected components of non-zero non-2 cells
    seen = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] not in (0,2) and not seen[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                comp = []
                seen[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and grid[nx][ny]==col:
                            seen[nx][ny] = True
                            stack.append((nx,ny))
                clusters.append((min(comp), comp))
    # find start positions (cells with 2)
    starts = [(i,j) for i in range(h) for j in range(w) if grid[i][j]==2]
    if starts:
        cur = min(starts)
    else:
        # if no 2, start at first cluster
        clusters.sort(key=lambda x: x[0])
        cur = clusters[0][0]
    # sort clusters by rep
    clusters.sort(key=lambda x: x[0])
    # BFS connect to each cluster
    for rep, comp in clusters:
        # skip if cur is adjacent to this cluster already
        if any(abs(cur[0]-x)+abs(cur[1]-y)==1 for x,y in comp):
            continue
        from collections import deque
        q = deque([cur])
        prev = {cur:None}
        end = None
        while q:
            x,y = q.popleft()
            for dx,dy in dirs:
                nx,ny = x+dx, y+dy
                if 0 <= nx < h and 0 <= ny < w and (nx,ny) not in prev:
                    if grid[nx][ny]==0:
                        prev[(nx,ny)] = (x,y)
                        # check adjacency to cluster
                        if any(abs(nx-x2)+abs(ny-y2)==1 for x2,y2 in comp):
                            end = (nx,ny)
                            q.clear()
                            break
                        q.append((nx,ny))
            if end is not None:
                break
        if end is None:
            continue
        # mark path
        p = end
        while p and p != cur:
            x,y = p
            grid[x][y] = 2
            p = prev[p]
        cur = end
    return grid