def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                comp = []
                stack = [(i,j)]
                visited[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny]!=0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                comps.append(comp)
    main = max(comps, key=len)
    main_set = set(main)
    mapping = {}
    for i in range(h):
        for j in range(w-1):
            if (i,j) not in main_set and (i,j+1) not in main_set:
                v1, v2 = grid[i][j], grid[i][j+1]
                if v1 and v2:
                    left_ok = j-1<0 or grid[i][j-1]==0 or (i,j-1) in main_set
                    right_ok = j+2>=w or grid[i][j+2]==0 or (i,j+2) in main_set
                    if left_ok and right_ok:
                        mapping[v2] = v1
    rows = [x for x,_ in main]
    cols = [y for _,y in main]
    mi, ma = min(rows), max(rows)
    mj, mb = min(cols), max(cols)
    out = []
    for i in range(mi, ma+1):
        row = []
        for j in range(mj, mb+1):
            v = grid[i][j]
            row.append(mapping[v] if v in mapping else v)
        out.append(row)
    return out