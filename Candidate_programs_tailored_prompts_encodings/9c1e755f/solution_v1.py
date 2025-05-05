from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited5 = [[False]*W for _ in range(H)]
    visited_seed = [[False]*W for _ in range(H)]
    anchors = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 5 and not visited5[r][c]:
                stack = [(r,c)]
                comp = []
                visited5[r][c] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == 5 and not visited5[nx][ny]:
                            visited5[nx][ny] = True
                            stack.append((nx,ny))
                rows = [x for x,_ in comp]
                cols = [y for _,y in comp]
                rmin, rmax = min(rows), max(rows)
                cmin, cmax = min(cols), max(cols)
                orient = 'vertical' if cmin == cmax and rmax > rmin else 'horizontal'
                anchors.append({'cells':comp,'orientation':orient,'r_min':rmin,'r_max':rmax,'c_min':cmin,'c_max':cmax})
    for anc in anchors:
        seeds = []
        for (ar,ac) in anc['cells']:
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc = ar+dx, ac+dy
                if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] not in (0,5) and not visited_seed[nr][nc]:
                    stack = [(nr,nc)]
                    comp = []
                    visited_seed[nr][nc] = True
                    while stack:
                        x,y = stack.pop()
                        comp.append((x,y))
                        for ddx,ddy in ((1,0),(-1,0),(0,1),(0,-1)):
                            xx,yy = x+ddx, y+ddy
                            if 0 <= xx < H and 0 <= yy < W and grid[xx][yy] not in (0,5) and not visited_seed[xx][yy]:
                                visited_seed[xx][yy] = True
                                stack.append((xx,yy))
                    rs = sorted({x for x,_ in comp})
                    cs = sorted({y for _,y in comp})
                    if len(rs) == 1:
                        r0 = rs[0]
                        seq = [grid[r0][y] for y in cs]
                        seeds.append({'orientation':'horizontal','row':r0,'cols':cs,'seq':seq})
                    else:
                        c0 = cs[0]
                        seq = [grid[x][c0] for x in rs]
                        seeds.append({'orientation':'vertical','col':c0,'rows':rs,'seq':seq})
        if anc['orientation'] == 'vertical' and seeds:
            seeds_h = [s for s in seeds if s['orientation']=='horizontal']
            seeds_h.sort(key=lambda s: s['row'])
            seqs = [s['seq'] for s in seeds_h]
            cmin = min(s['cols'][0] for s in seeds_h)
            rmin, rmax = anc['r_min'], anc['r_max']
            n = len(seqs)
            for i, r in enumerate(range(rmin, rmax+1)):
                seq = seqs[i % n]
                for j, v in enumerate(seq):
                    out[r][cmin+j] = v
        if anc['orientation'] == 'horizontal' and seeds:
            seeds_v = [s for s in seeds if s['orientation']=='vertical']
            seeds_v.sort(key=lambda s: s['col'])
            seqs = [s['seq'] for s in seeds_v]
            rmin = min(s['rows'][0] for s in seeds_v)
            cmin, cmax = anc['c_min'], anc['c_max']
            n = len(seqs)
            for j, c in enumerate(range(cmin, cmax+1)):
                seq = seqs[j % n]
                for i, v in enumerate(seq):
                    out[rmin+i][c] = v
    return out