from collections import deque
def solve(grid):
    H = len(grid)
    W = len(grid[0]) if H else 0
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = [[False]*W for _ in range(H)]
    clusters_by_color = {}
    for i in range(H):
        for j in range(W):
            c = grid[i][j]
            if c and not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j] = True
                cells = []
                while q:
                    r, cc = q.popleft()
                    cells.append((r,cc))
                    for dr,dc in dirs:
                        nr, nc = r+dr, cc+dc
                        if 0<=nr<H and 0<=nc<W and not visited[nr][nc] and grid[nr][nc]==c:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                clusters_by_color.setdefault(c,[]).append(cells)
    def bbox(cells):
        rs = [r for r,_ in cells]
        cs = [c for _,c in cells]
        return min(rs), max(rs), min(cs), max(cs)
    color_mins = {c: min(c0 for _,c0 in sum(clusters_by_color[c],[])) for c in clusters_by_color}
    colors = sorted(clusters_by_color, key=lambda c: color_mins[c])
    left_color, right_color = colors[0], colors[1]
    left_width = 0
    for cells in clusters_by_color[left_color]:
        r0,r1,c0,c1 = bbox(cells)
        left_width = max(left_width, c1-c0+1)
    band_x = {left_color:0, right_color:left_width+1}
    placements = {}
    for color in (left_color, right_color):
        data = []
        for cells in clusters_by_color[color]:
            r0,r1,c0,c1 = bbox(cells)
            w = c1-c0+1
            sz = len(cells)
            data.append((w, sz, r0, r1, c0, c1, cells))
        data.sort(key=lambda x:(x[3]-x[2]+1, x[0], x[1]), reverse=True)
        prev = None
        for idx,(w,sz,r0,r1,c0,c1,cells) in enumerate(data):
            h = r1-r0+1
            if idx==0:
                y = H - h
            else:
                y = prev - 1 - h
            placements[(color,r0,c0)] = (y, band_x[color], cells, r0, c0)
            prev = y
    out = [[0]*W for _ in range(H)]
    for (color,_,_), (y,x,cells,or0,oc0) in placements.items():
        for r,c in cells:
            out[y + (r-or0)][x + (c-oc0)] = color
    return out