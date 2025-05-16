from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    cnt = {}
    for row in grid:
        for v in row:
            cnt[v] = cnt.get(v, 0) + 1
    bg = max(cnt, key=lambda k: cnt[k])
    vis = [[False]*C for _ in range(R)]
    comps = []
    for i in range(R):
        for j in range(C):
            if not vis[i][j] and grid[i][j] != bg:
                col = grid[i][j]
                stack = [(i, j)]
                vis[i][j] = True
                cells = []
                while stack:
                    x, y = stack.pop()
                    cells.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < R and 0 <= ny < C and not vis[nx][ny] and grid[nx][ny] == col:
                            vis[nx][ny] = True
                            stack.append((nx, ny))
                xs = [x for x,_ in cells]; ys = [y for _,y in cells]
                x0, x1 = min(xs), max(xs)
                y0, y1 = min(ys), max(ys)
                h, w = x1-x0+1, y1-y0+1
                comps.append({'col': col, 'x0': x0, 'y0': y0, 'h': h, 'w': w})
    sizes = [c['h'] for c in comps if c['h']==c['w'] and c['h']>2]
    if not sizes:
        return grid
    D = max(sizes)
    d = D - 2
    bigs = [c for c in comps if c['h']==c['w']==D]
    smalls = [c for c in comps if c['h']==c['w']==d]
    bigs.sort(key=lambda c:(c['x0'],c['y0']))
    smalls.sort(key=lambda c:(c['x0'],c['y0']))
    mats = []
    for bc, sc in zip(bigs, smalls):
        mat = [[bc['col']]*D for _ in range(D)]
        for i in range(d):
            for j in range(d):
                v = grid[sc['x0']+i][sc['y0']+j]
                if v != bg:
                    mat[i+1][j+1] = v
        mats.append({'x0': bc['x0'], 'y0': bc['y0'], 'mat': mat})
    rows = sorted(set(b['x0'] for b in bigs))
    out = []
    for rx in rows:
        rowm = [m for m in mats if m['x0']==rx]
        rowm.sort(key=lambda m:m['y0'])
        for i in range(D):
            line = []
            for m in rowm:
                line += m['mat'][i]
            out.append(line)
    return out