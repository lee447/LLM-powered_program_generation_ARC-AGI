from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    # detect fill color
    first_row = grid[0]
    colors = set(c for row in grid for c in row if c != 0)
    anchors = [c for c in range(W) if grid[0][c] != 0]
    fill_colors = {grid[0][c] for c in anchors}
    fills = colors - fill_colors
    fill_color = fills.pop() if fills else 8
    # palette anchors
    anchors = [c for c in anchors if grid[0][c] != fill_color]
    palette = [grid[0][c] for c in anchors]
    K = len(palette)
    # find fill components
    visited = [[False]*W for _ in range(H)]
    comps = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] == fill_color and not visited[r][c]:
                stack = [(r,c)]
                visited[r][c] = True
                cells = []
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and grid[nx][ny]==fill_color:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                rs = [x for x,_ in cells]
                cs = [y for _,y in cells]
                r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
                by_row = {}
                for x,y in cells:
                    by_row.setdefault(x, []).append(y)
                comps.append((r0,r1,c0,c1,by_row,cells))
    if not comps or K == 0:
        return [[0]*W for _ in range(H)]
    minr = min(c[0] for c in comps)
    maxr = max(c[1] for c in comps)
    topl = [c for c in comps if c[0]==minr]
    botl = [c for c in comps if c[1]==maxr]
    topl.sort(key=lambda x: x[2])
    botl.sort(key=lambda x: x[2])
    tops = [len(c[4][c[0]]) for c in topl]
    bots = [len(c[4][c[1]]) for c in botl]
    widths = []
    ti = bi = 0
    pick = True
    while len(widths) < K:
        if pick:
            if ti < len(tops):
                widths.append(tops[ti]); ti += 1
            else:
                widths.append(bots[min(bi, len(bots)-1)]); bi += 1
        else:
            if bi < len(bots):
                widths.append(bots[bi]); bi += 1
            else:
                widths.append(tops[min(ti, len(tops)-1)]); ti += 1
        pick = not pick
    # partition unique fill columns into K groups by widths
    cols = sorted({c for comp in comps for _,_ ,_,_,_,cells in [(None,None,None,None,None,comp[5])] for (_,c) in cells})
    groups = []
    idx = 0
    for i,w in enumerate(widths):
        if i < K-1:
            groups.append(set(cols[idx:idx+w]))
            idx += w
        else:
            groups.append(set(cols[idx:]))
    out = [[0]*W for _ in range(H)]
    for comp in comps:
        for r,c in comp[5]:
            for i,g in enumerate(groups):
                if c in g:
                    out[r][c] = palette[i]
                    break
    return out