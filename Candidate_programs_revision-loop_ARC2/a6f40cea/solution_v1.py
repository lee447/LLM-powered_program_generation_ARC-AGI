def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import Counter, deque
    cnt = Counter([c for row in grid for c in row])
    bg = max(cnt, key=cnt.get)
    # find cross-shaped color (distractor)
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    distract = None
    for r in range(h):
        for c in range(w):
            col = grid[r][c]
            if col!=bg and not seen[r][c]:
                q=deque([(r,c)]); seen[r][c]=True
                pts=[(r,c)]
                while q:
                    x,y = q.popleft()
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==col:
                            seen[nx][ny]=True; q.append((nx,ny)); pts.append((nx,ny))
                # check for a cross center
                for x,y in pts:
                    cntn=0
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny]==col:
                            cntn+=1
                    if cntn>2:
                        distract = col
                        break
                if distract is not None:
                    break
        if distract is not None:
            break
    # remove distractor
    if distract is not None:
        for i in range(h):
            for j in range(w):
                if grid[i][j]==distract:
                    grid[i][j] = bg
    # crop to the remaining
    minr,minc, maxr, maxc = h, w, -1, -1
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=bg:
                minr = min(minr, i)
                maxr = max(maxr, i)
                minc = min(minc, j)
                maxc = max(maxc, j)
    if minr>maxr:
        return []
    return [row[minc:maxc+1] for row in grid[minr:maxr+1]]