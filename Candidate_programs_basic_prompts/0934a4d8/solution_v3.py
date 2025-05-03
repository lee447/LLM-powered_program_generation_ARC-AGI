def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import deque
    def find_block_color():
        seen = [[False]*w for _ in range(h)]
        best = (0, None, None)
        for i in range(h):
            for j in range(w):
                if not seen[i][j]:
                    c = grid[i][j]
                    q = deque([(i,j)])
                    seen[i][j] = True
                    pts = [(i,j)]
                    while q:
                        x,y = q.popleft()
                        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            nx,ny = x+dx, y+dy
                            if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==c:
                                seen[nx][ny]=True
                                pts.append((nx,ny))
                                q.append((nx,ny))
                    minr = min(r for r,c in pts)
                    maxr = max(r for r,c in pts)
                    minc = min(c for r,c in pts)
                    maxc = max(c for r,c in pts)
                    if maxr-minr+1 == len({r for r,_ in pts}) and maxc-minc+1 == len({c for _,c in pts}):
                        area = len(pts)
                        if area > best[0]:
                            best = (area, (minr,maxr), (minc,maxc))
        return best[1], best[2], grid[best[1][0]][best[2][0]]
    (r0,r1),(c0,c1),block_color = find_block_color()
    bh, bw = r1-r0+1, c1-c0+1
    for i in range(h):
        for j in range(w):
            if grid[i][j]==block_color:
                pass
    def count_sub(i,j):
        for di in range(bh):
            for dj in range(bw):
                if grid[i+di][j+dj]==block_color:
                    return False
        return True
    cnt = {}
    for i in range(h-bh+1):
        for j in range(w-bw+1):
            if count_sub(i,j):
                key = tuple(tuple(grid[i+di][j:j+bw]) for di in range(bh))
                cnt.setdefault(key,0)
                cnt[key]+=1
    for pat,c in cnt.items():
        if c==1:
            return [list(row) for row in pat]
    return []