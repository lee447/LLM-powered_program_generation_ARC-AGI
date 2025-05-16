from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    freq = {}
    for row in grid:
        for v in row:
            freq[v] = freq.get(v, 0) + 1
    bg = max(freq, key=lambda k: freq[k])
    visited = [[False]*w for _ in range(h)]
    comps = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != bg and not visited[i][j]:
                q = [(i, j)]
                visited[i][j] = True
                comp = []
                for x,y in q:
                    comp.append((x,y))
                    for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == c:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                comps.setdefault(c, []).append(comp)
    ref = max(comps.keys())
    ref_lens = [len(c) for c in comps[ref]]
    if len(ref_lens) == 1:
        target = ref_lens[0]
    else:
        cnt = {}
        for L in ref_lens:
            cnt[L] = cnt.get(L, 0) + 1
        m = max(cnt.values())
        target = min(L for L,v in cnt.items() if v == m)
    newpts = []
    for color, clist in comps.items():
        for comp in clist:
            if len(comp) > 1:
                rows = [r for r,c in comp]
                cols = [c for r,c in comp]
                minr, maxr = min(rows), max(rows)
                minc, maxc = min(cols), max(cols)
                dx = 1 if maxr > minr else (-1 if maxr < minr else 0)
                dy = 1 if maxc > minc else (-1 if maxc < minc else 0)
            else:
                dx, dy = 0, 0
            if dx != 0:
                if dx > 0:
                    comp_sorted = sorted(comp, key=lambda x: x[0])
                else:
                    comp_sorted = sorted(comp, key=lambda x: -x[0])
            else:
                if dy > 0:
                    comp_sorted = sorted(comp, key=lambda x: x[1])
                else:
                    comp_sorted = sorted(comp, key=lambda x: -x[1])
            comp2 = comp_sorted[:]
            neg = dx * dy < 0
            if neg:
                while len(comp2) > target:
                    comp2.pop(0)
                while len(comp2) < target:
                    hr, hc = comp2[0]
                    tr, tc = comp2[-1]
                    nr, nc = hr - dx, hc - dy
                    if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == bg and (nr,nc) not in comp2:
                        comp2.insert(0, (nr,nc))
                        continue
                    nr, nc = tr + dx, tc + dy
                    if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == bg and (nr,nc) not in comp2:
                        comp2.append((nr,nc))
                        continue
                    break
            else:
                while len(comp2) > target:
                    comp2.pop()
                while len(comp2) < target:
                    hr, hc = comp2[0]
                    tr, tc = comp2[-1]
                    nr, nc = tr + dx, tc + dy
                    if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == bg and (nr,nc) not in comp2:
                        comp2.append((nr,nc))
                        continue
                    nr, nc = hr - dx, hc - dy
                    if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == bg and (nr,nc) not in comp2:
                        comp2.insert(0, (nr,nc))
                        continue
                    break
            for r,c in comp2:
                newpts.append((r,c,color))
    out = [[bg]*w for _ in range(h)]
    for r,c,v in newpts:
        out[r][c] = v
    return out