def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==3 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==3:
                            visited[nx][ny]=True
                            stack.append((nx,ny))
                comps.append(comp)
    boxes = []
    for comp in comps:
        rs = [x for x,_ in comp]
        cs = [y for _,y in comp]
        boxes.append((min(rs),max(rs),min(cs),max(cs),comp))
    boxes.sort(key=lambda b: (b[2]+b[3])/2)
    left = boxes[0]
    center = boxes[1]
    right = boxes[2]
    lminr,lmaxr,lminc,lmaxc,_ = left
    sminr,smaxr,sminc,smaxc,_ = center
    rminr,rmaxr,rminc,rmaxc,_ = right
    new = [[0]*w for _ in range(h)]
    # copy left frame
    for x,y in left[4]:
        new[x][y] = 3
    # copy right frame
    for x,y in right[4]:
        new[x][y] = 3
    # copy center border
    for x,y in center[4]:
        if x==sminr or x==smaxr or y==sminc or y==smaxc:
            new[x][y] = 3
    # fill corridor for left
    for i in range(lminr+1, lmaxr):
        for j in range(lmaxc+1, sminc):
            new[i][j] = 3
    # fill corridor for right
    for i in range(rminr+1, rmaxr):
        for j in range(smaxc+1, rminc):
            new[i][j] = 3
    return new