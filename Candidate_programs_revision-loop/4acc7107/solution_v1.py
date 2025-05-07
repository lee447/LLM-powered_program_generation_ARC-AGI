def solve(grid):
    H=len(grid)
    W=len(grid[0]) if H>0 else 0
    from collections import deque
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    clusters_by_color={}
    visited=[[False]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            c=grid[i][j]
            if c!=0 and not visited[i][j]:
                q=deque([(i,j)])
                visited[i][j]=True
                cells=[]
                while q:
                    r,c0=q.popleft()
                    cells.append((r,c0))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c0+dc
                        if 0<=nr<H and 0<=nc<W and not visited[nr][nc] and grid[nr][nc]==grid[i][j]:
                            visited[nr][nc]=True
                            q.append((nr,nc))
                if grid[i][j] not in clusters_by_color:
                    clusters_by_color[grid[i][j]]=[]
                clusters_by_color[grid[i][j]].append(cells)
    color_mins = {c: min(x for _,x in sum(clusters_by_color[c],[])) for c in clusters_by_color}
    colors=sorted(clusters_by_color.keys(), key=lambda c: color_mins[c])
    left_color, right_color = colors[0], colors[1]
    def bbox(cells):
        rs=[r for r,_ in cells]; cs=[c for _,c in cells]
        return min(rs), max(rs), min(cs), max(cs)
    GAP=1
    left_width = 0
    for cells in clusters_by_color[left_color]:
        r0,r1,c0,c1=bbox(cells)
        left_width = max(left_width, c1-c0+1)
    band_x = {left_color:0, right_color:left_width+GAP}
    placements={}
    for color in [left_color, right_color]:
        cls=clusters_by_color[color]
        data=[]
        for cells in cls:
            r0,r1,c0,c1=bbox(cells)
            data.append((len(cells), r0, r1, c0, c1, cells))
        data.sort(reverse=True, key=lambda x: x[0])
        prev_y_start=None
        for idx,(sz,r0,r1,c0,c1,cells) in enumerate(data):
            h = r1-r0+1
            if idx==0:
                y_start = H - h
            else:
                y_start = prev_y_start - GAP - h
            placements[(color,r0,c0)] = (y_start, band_x[color], r0, c0)
            prev_y_start = y_start
    out = [[0]*W for _ in range(H)]
    for (color,r0,c0), (y_start,x_start,_,_) in placements.items():
        cells = next(cells for cells in clusters_by_color[color] if bbox(cells)[0]==r0 and bbox(cells)[2]==c0)
        for r,c in cells:
            nr = y_start + (r-r0)
            nc = x_start + (c-c0)
            out[nr][nc]=color
    return out