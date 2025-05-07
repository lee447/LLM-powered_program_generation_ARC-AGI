def solve(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    bboxes = []
    for i in range(m):
        for j in range(n):
            if grid[i][j]==8 and not visited[i][j]:
                q = [(i,j)]
                visited[i][j] = True
                rmin = rmax = i
                cmin = cmax = j
                for x,y in q:
                    for dx,dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and grid[nx][ny]==8:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                            rmin = min(rmin,nx)
                            rmax = max(rmax,nx)
                            cmin = min(cmin,ny)
                            cmax = max(cmax,ny)
                bboxes.append([rmin,rmax,cmin,cmax])
    def mergable(a,b):
        ar1, ar2, ac1, ac2 = a
        br1, br2, bc1, bc2 = b
        # overlap
        if ar1<=br2 and br1<=ar2 and ac1<=bc2 and bc1<=ac2:
            return True
        # touch vertically (one above/below)
        if (ar2+1==br1 or br2+1==ar1) and (ac1<=bc2 and bc1<=ac2):
            return True
        # touch horizontally (one left/right)
        if (ac2+1==bc1 or bc2+1==ac1) and (ar1<=br2 and br1<=ar2):
            return True
        return False
    def merge(a,b):
        return [min(a[0],b[0]), max(a[1],b[1]), min(a[2],b[2]), max(a[3],b[3])]
    changed = True
    while changed:
        changed = False
        nbb = len(bboxes)
        for i in range(nbb):
            for j in range(i+1, nbb):
                if mergable(bboxes[i], bboxes[j]):
                    nb = merge(bboxes[i], bboxes[j])
                    bboxes.pop(j)
                    bboxes.pop(i)
                    bboxes.append(nb)
                    changed = True
                    break
            if changed:
                break
    out = [row[:] for row in grid]
    for r1,r2,c1,c2 in bboxes:
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if out[i][j]==0:
                    out[i][j] = 2
    return out