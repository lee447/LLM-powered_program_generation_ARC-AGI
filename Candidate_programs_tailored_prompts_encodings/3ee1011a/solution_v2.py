def solve(grid):
    h = len(grid)
    w = len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                color = grid[i][j]
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny]==color:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                comps.append((color,comp))
    segments = []
    blobs = []
    for color,comp in comps:
        if len(comp)>2:
            rows = {x for x,y in comp}
            cols = {y for x,y in comp}
            if len(rows)==1 or len(cols)==1:
                segments.append((len(comp),color))
            else:
                blobs.append((comp,color))
        else:
            blobs.append((comp,color))
    segments.sort(reverse=True)
    num_frames = len(segments)
    frames = [c for l,c in segments]
    if blobs:
        blob_comp, blob_color = max(blobs, key=lambda bc: len(bc[0]))
        xs = [x for x,y in blob_comp]
        ys = [y for x,y in blob_comp]
        bh = max(xs)-min(xs)+1
        bw = max(ys)-min(ys)+1
        bs = max(bh,bw)
    else:
        blob_color=0
        bs=1
    size = bs + 2*num_frames
    out = [[0]*size for _ in range(size)]
    for i,c in enumerate(frames):
        o = i
        t = size-1-i
        for x in range(o,t+1):
            out[o][x] = c
            out[t][x] = c
        for y in range(o,t+1):
            out[y][o] = c
            out[y][t] = c
    o = num_frames
    for x in range(o,o+bs):
        for y in range(o,o+bs):
            out[x][y] = blob_color
    return out